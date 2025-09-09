"""
RAG (Retrieval-Augmented Generation) REST API
- FastAPI를 사용한 REST API 서버
- 자연스러운 대화가 이어지는 RAG 시스템
- 질의 확장을 통한 맥락적 질문 처리

API 총 6개
1. / : API 상태 확인
2. /chat : 채팅 엔드포인트 - 질문을 받고 답변을 반환
3. /sessions : 활성 세션 목록 조회
4. /sessions/{session_id}/history : 특정 세션의 대화 기록 조회
5. /sessions/{session_id} : 세션 삭제
6. /sessions/{session_id}/clear : 세션 대화 기록 초기화
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

# RAG 관련 라이브러리
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# ===== FastAPI 앱 초기화 =====
app = FastAPI(
    title="RAG Chat API",
    description="Retrieval-Augmented Generation을 사용한 대화형 AI API",
    version="1.0.0"
)

# ===== 환경변수 및 기본 설정 =====
load_dotenv()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

# 모델 설정
embedding = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)
persist_directory = "chroma_store"

# ===== 벡터 데이터베이스 로드 =====
print("Loading existing Chroma Store...")
try:
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    retriever = vectorstore.as_retriever(k=3)
    print("✅ Chroma Store loaded successfully!")
except Exception as e:
    print(f"❌ Chroma Store 로드 실패: {e}")
    raise

# ===== 전역 변수 (세션 관리) =====
# 실제 운영환경에서는 Redis나 데이터베이스 사용 권장
sessions = {}  # {session_id: ChatMessageHistory}

# ===== Pydantic 모델 정의 =====
class ChatRequest(BaseModel):
    """채팅 요청 모델"""
    message: str
    session_id: Optional[str] = None
    use_query_expansion: bool = True  # 질의 확장 사용 여부

class ChatResponse(BaseModel):
    """채팅 응답 모델"""
    session_id: str
    message: str
    response: str
    expanded_query: Optional[str] = None
    timestamp: str

class SessionInfo(BaseModel):
    """세션 정보 모델"""
    session_id: str
    created_at: str
    message_count: int

# ===== RAG 체인 설정 =====
# 질의 확장 프롬프트
query_augmentation_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="messages"),
    ("system", """이전 대화 내용을 참고하여 사용자의 질문을 명확하고 구체적으로 확장하세요.
    
규칙:
1. 대명사(이, 저, 그, 그것 등)를 명확한 명사로 변환
2. 맥락에 맞는 구체적인 질문으로 확장
3. 한 문장으로 명료하게 표현
4. 이전 대화와 관련된 주제라면 그 맥락을 유지

예시:
- "그것은?" → "서울시의 온실가스 저감 정책은?"
- "뉴욕은?" → "뉴욕의 환경 정책은?"
- "비용은?" → "서울시 온실가스 저감 정책의 비용은?"

질문: {query}"""),
])

query_augmentation_chain = query_augmentation_prompt | chat | StrOutputParser()

# 답변 생성 프롬프트
question_answering_prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 도시 정책 전문가입니다. 주어진 문서를 기반으로 사용자의 질문에 정확하고 도움이 되는 답변을 제공하세요.

답변 규칙:
1. 주어진 context(문서)를 기반으로만 답변
2. 정확한 정보만 제공하고 추측하지 말 것
3. 구체적인 수치나 정책명이 있다면 포함
4. 답변할 수 없는 내용은 솔직히 말하기
5. 자연스럽고 친근한 톤으로 답변

Context: {context}"""),
    ("human", "{input}"),
])

document_chain = create_stuff_documents_chain(llm=chat, prompt=question_answering_prompt)

# ===== 유틸리티 함수 =====
def get_or_create_session(session_id: Optional[str] = None) -> tuple[str, ChatMessageHistory]:
    """세션을 가져오거나 새로 생성"""
    if session_id and session_id in sessions:
        return session_id, sessions[session_id]
    
    # 새 세션 생성
    new_session_id = str(uuid.uuid4())
    sessions[new_session_id] = ChatMessageHistory()
    return new_session_id, sessions[new_session_id]

def process_rag_query(message: str, chat_history: ChatMessageHistory, use_expansion: bool = True) -> tuple[str, Optional[str]]:
    """RAG 쿼리 처리"""
    # 1. 질의 확장 (선택적)
    if use_expansion and len(chat_history.messages) > 0:
        try:
            expanded_query = query_augmentation_chain.invoke({
                "query": message, 
                "messages": chat_history.messages
            })
        except Exception as e:
            print(f"질의 확장 실패: {e}")
            expanded_query = message
    else:
        expanded_query = message
    
    # 2. 문서 검색
    docs = retriever.invoke(expanded_query)
    
    # 3. 답변 생성
    answer = document_chain.invoke({"context": docs, "input": message})
    
    return answer, expanded_query if use_expansion else None

# ===== API 엔드포인트 =====
@app.get("/")
async def root():
    """API 상태 확인"""
    return {
        "message": "RAG Chat API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """채팅 엔드포인트 - 질문을 받고 답변을 반환"""
    try:
        # 세션 관리
        session_id, chat_history = get_or_create_session(request.session_id)
        
        # 사용자 메시지를 세션에 추가
        chat_history.add_user_message(request.message)
        
        # RAG 처리
        response, expanded_query = process_rag_query(
            request.message, 
            chat_history, 
            request.use_query_expansion
        )
        
        # AI 응답을 세션에 추가
        chat_history.add_ai_message(response)
        
        return ChatResponse(
            session_id=session_id,
            message=request.message,
            response=response,
            expanded_query=expanded_query,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"처리 중 오류가 발생했습니다: {str(e)}")

@app.get("/sessions", response_model=List[SessionInfo])
async def get_sessions():
    """활성 세션 목록 조회"""
    session_list = []
    for session_id, history in sessions.items():
        session_list.append(SessionInfo(
            session_id=session_id,
            created_at=datetime.now().isoformat(),  # 실제로는 생성 시간 저장 필요
            message_count=len(history.messages)
        ))
    return session_list

@app.get("/sessions/{session_id}/history")
async def get_session_history(session_id: str):
    """특정 세션의 대화 기록 조회"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="세션을 찾을 수 없습니다.")
    
    history = sessions[session_id]
    messages = []
    for msg in history.messages:
        messages.append({
            "type": msg.__class__.__name__,
            "content": msg.content,
            "timestamp": datetime.now().isoformat()  # 실제로는 메시지별 시간 저장 필요
        })
    
    return {
        "session_id": session_id,
        "message_count": len(messages),
        "messages": messages
    }

@app.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """세션 삭제"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="세션을 찾을 수 없습니다.")
    
    del sessions[session_id]
    return {"message": f"세션 {session_id}이 삭제되었습니다."}

@app.post("/sessions/{session_id}/clear")
async def clear_session_history(session_id: str):
    """세션 대화 기록 초기화"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="세션을 찾을 수 없습니다.")
    
    sessions[session_id] = ChatMessageHistory()
    return {"message": f"세션 {session_id}의 대화 기록이 초기화되었습니다."}

# ===== 서버 실행 =====
if __name__ == "__main__":
    import uvicorn
    print("🚀 RAG Chat API 서버를 시작합니다...")
    print("📖 문서: http://localhost:8000/docs")
    print("💬 채팅: POST http://localhost:8000/chat")
    uvicorn.run(app, host="0.0.0.0", port=8000)

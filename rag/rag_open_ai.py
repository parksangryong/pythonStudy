"""
RAG (Retrieval-Augmented Generation) 시스템 구현
- 벡터 데이터베이스(Chroma)를 사용한 문서 검색
- 질의 확장을 통한 맥락적 질문 처리
- 대화 메모리를 활용한 연속적인 질문-답변
"""

# ===== 필요한 라이브러리 import =====
from langchain_chroma import Chroma  # 벡터 데이터베이스 (Chroma)
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  # OpenAI 임베딩 및 채팅 모델
from langchain.memory import ChatMessageHistory  # 대화 메모리 관리
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # 프롬프트 템플릿
from langchain.chains.combine_documents import create_stuff_documents_chain  # 문서 결합 체인
from langchain_core.output_parsers import StrOutputParser  # 문자열 출력 파서
from dotenv import load_dotenv  # 환경변수 로드
import os

# ===== 환경변수 및 기본 설정 =====
load_dotenv()  # .env 파일에서 환경변수 로드

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 임베딩 모델 설정 (문서를 벡터로 변환)
embedding = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)

# 채팅 모델 설정 (GPT-4o-mini 사용)
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 벡터 데이터베이스 저장 경로
persist_directory = "chroma_store"

# ===== 벡터 데이터베이스 로드 =====
print("Loading existing Chroma Store")
# 기존에 저장된 Chroma 벡터 데이터베이스 로드
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# 검색기 설정 (상위 3개 문서 검색)
retriever = vectorstore.as_retriever(k=3)

# ===== 대화 메모리 초기화 =====
# 사용자와 AI의 대화 기록을 저장할 메모리 객체
chat_history = ChatMessageHistory()

# ===== 질의 확장 프롬프트 설정 =====
# 대명사나 모호한 표현을 명확한 질문으로 변환하는 프롬프트
query_augmentation_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="messages"),  # 이전 대화 내용 포함
    ("system", "기존의 대화 내용을 활용하여 사용자가 질문한 의도를 파악해서 한 문장의 명료한 질문으로 변환하라. 대명사나 이, 저, 그와 같은 표현을 명확한 명사로 표현하라: \n\n{query}"),
])

# 질의 확장 체인 구성 (프롬프트 → 채팅모델 → 문자열파서)
query_augmentation_chain = query_augmentation_prompt | chat | StrOutputParser()

# ===== 답변 생성 프롬프트 설정 =====
# 검색된 문서를 기반으로 답변을 생성하는 프롬프트
question_answering_prompt = ChatPromptTemplate.from_messages([
    ("system", "사용자의 질문에 대해 아래 context를 기반하여 답변하라.: \n\n{context}"),
    ("human", "{input}"),
])

# 문서 결합 체인 생성 (검색된 문서들을 하나의 답변으로 결합)
document_chain = create_stuff_documents_chain(llm=chat, prompt=question_answering_prompt)

# ===== 첫 번째 질문 처리 =====
print("=== 첫 번째 질문 ===")
first_question = "서울시의 온실가스 저감 정책에 대해 알려줘"

# 사용자 질문을 메모리에 저장
chat_history.add_user_message(first_question)

# 1. 문서 검색: 질문과 유사한 문서들을 벡터 데이터베이스에서 검색
docs = retriever.invoke(first_question)

# 2. 답변 생성: 검색된 문서를 기반으로 AI가 답변 생성
answer1 = document_chain.invoke({"context": docs, "input": first_question})

# AI 답변을 메모리에 저장
chat_history.add_ai_message(answer1)

# 결과 출력
print(f"질문: {first_question}")
print(f"답변: {answer1}\n")

# ===== 두 번째 질문 처리 (질의 확장 사용) =====
print("=== 두 번째 질문 ===")
second_question = "뉴욕은?"  # 모호한 질문

# 사용자 질문을 메모리에 저장
chat_history.add_user_message(second_question)

# 1. 질의 확장: 이전 대화 맥락을 고려하여 모호한 질문을 명확하게 변환
augmented_query = query_augmentation_chain.invoke({"query": second_question, "messages": chat_history.messages})

print(f"원래 질문: {second_question}")
print(f"확장된 질문: {augmented_query}")

# 2. 문서 검색: 확장된 질문으로 관련 문서 검색
docs2 = retriever.invoke(augmented_query)

# 3. 답변 생성: 검색된 문서를 기반으로 답변 생성
answer2 = document_chain.invoke({"context": docs2, "input": second_question})

# AI 답변을 메모리에 저장
chat_history.add_ai_message(answer2)

# 결과 출력
print(f"답변: {answer2}")
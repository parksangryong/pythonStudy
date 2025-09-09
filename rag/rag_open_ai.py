# 크로마 데이터베이스 생성
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# 채팅 메시지 저장
from langchain.memory import ChatMessageHistory
# 프롬프트 정의하는 템플릿 및 데이터를 프롬프트에 삽입하기 위한 클래스
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 여러 텍스트를 결합해 최종 답변을 생성하는 체인
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embedding = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)

# 크로마 데이터베이스 생성 경로
persist_directory = "chroma_store"

# 채팅 메시지 저장할 메모리 객체 생성
chat_history = ChatMessageHistory()
# 사용자 질문을 메모리에 저장
chat_history.add_user_message("서울시의 온실가스 저감 정책에 대해 알려줘")

print("Loading existing Chroma Store")
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# 리트리버 통해 3개의 청크 가져오도록 설정
retriever = vectorstore.as_retriever(k=3)
docs = retriever.invoke("서울시의 환경 정책이 궁금해")

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)

question_answering_prompt = ChatPromptTemplate.from_messages([
    ("system", "사용자의 질문에 대해 아래 context를 기반하여 답변하라.: \n\n{context}"),
    ("human", "{input}"),
])

document_chain = create_stuff_documents_chain(llm=chat, prompt=question_answering_prompt)

# 체인 실행
question = "서울시의 온실가스 저감 정책에 대해 알려줘"
# 문서 검색하고 답변 생성
answer = document_chain.invoke({"context": docs, "input": question})

# 답변을 메모리에 저장
chat_history.add_ai_message(answer)

print(answer)
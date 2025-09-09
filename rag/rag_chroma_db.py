# 크로마 데이터베이스 생성
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader # PDF 파일 읽는 라이브러리
from langchain_text_splitters import RecursiveCharacterTextSplitter # 텍스트 쪼개는 라이브러리

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embedding = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)

# PDF 파일 읽어 텍스트 추출
nyc_loader = PyPDFLoader("data/OneNYC_2050_Strategic_Plan.pdf")
data_nyc = nyc_loader.load()

# 텍스트 쪼개기(1000자 단위로 쪼개고 100자 중복 제거)
nyc_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
nyc_all_splits = nyc_text_splitter.split_documents(data_nyc)

print(f"NYC Total splits: {len(nyc_all_splits)}")

# PDF 파일 읽어 텍스트 추출
loader = PyPDFLoader("data/2040_seoul_plan.pdf")
data_seoul = loader.load()

# 텍스트 쪼개기(1000자 단위로 쪼개고 100자 중복 제거)
seoul_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
seoul_all_splits = seoul_text_splitter.split_documents(data_seoul)

print(f"Seoul Total splits: {len(seoul_all_splits)}")


all_splits = []
all_splits.extend(nyc_all_splits)
all_splits.extend(seoul_all_splits)

print(f"Total splits: {len(all_splits)}")

# 크로마 데이터베이스 생성 경로
persist_directory = "chroma_store"

# 크로마 데이터베이스 생성 경로가 없으면 생성, 있으면 로드
if not os.path.exists(persist_directory):
    print("Creating new Chroma Store")
    vectorstore = Chroma.from_documents(documents = all_splits, embedding=embedding, persist_directory=persist_directory)
else:
    print("Loading existing Chroma Store")
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# 리트리버 통해 3개의 청크 가져오도록 설정
retriever = vectorstore.as_retriever(k=3)
docs = retriever.invoke("서울시의 환경 정책이 궁금해")

for d in docs:
    print(d)
    print("-"*100)
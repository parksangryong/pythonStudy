from langchain_community.document_loaders import PyPDFLoader # PDF 파일 읽는 라이브러리
from langchain_text_splitters import RecursiveCharacterTextSplitter # 텍스트 쪼개는 라이브러리

# PDF 파일 읽어 텍스트 추출
nyc_loader = PyPDFLoader("data/OneNYC_2050_Strategic_Plan.pdf")
data_nyc = nyc_loader.load()

# 텍스트 쪼개기(1000자 단위로 쪼개고 100자 중복 제거)
nyc_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# 데이터 타입이 Document 형태로 반환(랭체인에서 제공하는 타입)
nyc_all_splits = nyc_text_splitter.split_documents(data_nyc)

print(f"NYC Total splits: {len(nyc_all_splits)}")

# PDF 파일 읽어 텍스트 추출
loader = PyPDFLoader("data/2040_seoul_plan.pdf")
data_seoul = loader.load()

# 텍스트 쪼개기(1000자 단위로 쪼개고 100자 중복 제거)
seoul_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# 데이터 타입이 Document 형태로 반환(랭체인에서 제공하는 타입)
seoul_all_splits = seoul_text_splitter.split_documents(data_seoul)

print(f"Seoul Total splits: {len(seoul_all_splits)}")


all_splits = []
all_splits.extend(nyc_all_splits)
all_splits.extend(seoul_all_splits)

print(f"Total splits: {len(all_splits)}")
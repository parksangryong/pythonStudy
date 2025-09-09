from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# text-embedding-3-large 모델 사용해서 임베딩 생성 : text-embedding-3-small, text-embedding-3-large, text-embedding_ada-002 등 존재
# 한글 문서일 경우, text-embedding-3-large 사용 권장
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)
# 원하는 텍스트 넣으면 벡터로 변환된 값을 반환
v = embeddings.embed_query("뉴욕의 온실가스 저감 정책은 머야?")
print(v)
print(len(v))
from langchain_community.tools import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

query = "현대 자동차 미국 시장 2025년 전망"

tavily_search = TavilySearchResults(
    max_results=5,
    api_key=TAVILY_API_KEY
)

res = tavily_search.invoke({
    "query": query
})

# 검색 결과를 문자열로 변환
content = "\n".join([result.get("content", "") for result in res])

# 프롬프트를 messages 형태로 구성
messages = [
    SystemMessage(content="당신은 신문 기사를 쓰는 기자 AI 입니다. \n\n 당신은 주어진 정보를 바탕으로 객관적이고 체계적으로 작성된 기사를 써야합니다. \n\n"),
    HumanMessage(content=f"정보: {content}\n\n 위의 정보를 사용하여, 다음 질문에 대한 보고서를 한국어로 작성하세요. {query} \n\n 신문 기사 형식을 사용하되, MLA 표준을 준수하는 markdown 문법을 사용해주세요. 활용한 자료는 출처를 명시하세요")
]

response = model.invoke(messages)
print(response.content)
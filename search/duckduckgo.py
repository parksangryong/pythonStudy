from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

chat_history = ChatMessageHistory()
chat_history.add_user_message("최근 로제가 받은 상은?")

question_answering_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 검색 전문가입니다. 사용자의 질문에 대해 아래 context를 기반하여 답변하라.: \n\n{context}"),
    MessagesPlaceholder(variable_name="messages"),
])

document_chain = question_answering_prompt | model

# DuckDuckGo 검색
wrapper = DuckDuckGoSearchAPIWrapper(region="kr-kr", time="w")
search = DuckDuckGoSearchResults(results_separator=";\n", num_results=10, api_wrapper=wrapper, source="news")
docs = search.invoke("최근 로제가 받은 상은?")

answer = document_chain.invoke({"context": docs, "messages": chat_history.messages})

chat_history.add_ai_message(answer)

print(answer.content)
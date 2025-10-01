from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = ChatOllama(model="llama3.2:1b")

# 방법 1: 메시지 리스트를 직접 사용 (대화 히스토리 포함)
print("=== 방법 1: 메시지 리스트 직접 사용 ===")
message_list = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is capital of France?"),
    AIMessage(content="The capital of France is Paris."),
    HumanMessage(content="What is capital of Korea?"),
    AIMessage(content="The capital of Korea is Seoul."),
    HumanMessage(content="What is capital of Japan?"),
    AIMessage(content="The capital of Japan is Tokyo."),
    HumanMessage(content="What is capital of China?"),
    AIMessage(content="The capital of China is Beijing."),
    HumanMessage(content="What is capital of USA?"),
]

result1 = llm.invoke(message_list)
print("결과:", result1.content)
print()


# 방법 2: ChatPromptTemplate 사용 (템플릿 기반)
print("=== 방법 2: ChatPromptTemplate 사용 ===")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "What is capital of {country}?"),
])

# 템플릿에 변수 입력
formatted_prompt = prompt.invoke({"country": "USA"})
result2 = llm.invoke(formatted_prompt)
print("결과:", result2.content)
print()


# 방법 3: 대화 히스토리가 있는 템플릿
print("=== 방법 3: 대화 히스토리 포함 템플릿 ===")
conversation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "What is capital of France?"),
    ("ai", "The capital of France is Paris."),
    ("human", "What is capital of Korea?"),
    ("ai", "The capital of Korea is Seoul."),
    ("human", "What is capital of Japan?"),
    ("ai", "The capital of Japan is Tokyo."),
    ("human", "What is capital of China?"),
    ("ai", "The capital of China is Beijing."),
    ("human", "What is capital of {country}?"),
])

formatted_conversation = conversation_prompt.invoke({"country": "USA"})
result3 = llm.invoke(formatted_conversation)
print("결과:", result3.content)
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = ChatOllama(model="llama3.2:1b")

# prompt template 생성
prompt_template = PromptTemplate(
    template="what is the capital of {country}?",
    input_variables=["country"]
)

# 메시지 리스트 생성
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
]

# 프롬프트 템플릿 실행 후 메시지 리스트에 추가
ASK = prompt_template.invoke({"country": "USA"}).text
message_list.append(HumanMessage(content=ASK))

# 메시지 리스트를 LLM에 전달
result = llm.invoke(message_list)
print("결과:", result.content)
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Ollama를 이용한 로컬 LLM 설정
llm = ChatOllama(model="llama3.2:1b")

# 문자열 출력 파서 설정
output_parser = StrOutputParser()

# 명시적인 지시사항이 포함된 프롬프트 템플릿 정의
prompt_template = PromptTemplate(
    template="What is the capital of {country}? Return the name of the city only",
    input_variables=["country"],
)

# 체인 생성 (프롬프트 템플릿 → LLM → 문자열 출력 파서)
chain = prompt_template | llm | output_parser

print(chain.invoke({"country": "France"}))
print(chain.invoke({"country": "Korea"}))
print(chain.invoke({"country": "Japan"}))
print(chain.invoke({"country": "China"}))
print(chain.invoke({"country": "USA"}))
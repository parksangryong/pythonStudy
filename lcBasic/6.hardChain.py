from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Ollama를 이용한 로컬 LLM 설정
llm = ChatOllama(model="llama3.2:1b")

# 문자열 출력 파서 설정
output_parser = StrOutputParser()

# 국가 이름 프롬프트 템플릿 정의
country_prompt = PromptTemplate(
    template="""Guess the name of the country in the {continent} based on the following information:
    {information}
    Return the name of the country only
    """,
    input_variables=["information", "continent"],
)

# 수도 프롬프트 템플릿 정의
capital_prompt = PromptTemplate(
    template="What is the capital of {country}? Return the name of the city only",
    input_variables=["country"],
)

# 1단계: 정보 -> (프롬프트) -> LLM -> 국가명 문자열
country_chain = (
    {"information": RunnablePassthrough(), "continent": RunnablePassthrough()}
    | country_prompt
    | llm
    | output_parser
)

# 2단계: 국가명 -> (수도 프롬프트) -> LLM -> 수도 문자열
final_chain = (
    {"country": country_chain}
    | capital_prompt
    | llm
    | output_parser
)


result = final_chain.invoke({
    "information": "This country is very famous for its Kimchi",
    "continent": "Asia",
})
print(result)


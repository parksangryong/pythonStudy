from langchain_ollama import ChatOllama  
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

# Ollama LLM 초기화
llm = ChatOllama(model="llama3.2:1b")

# 구조화된 출력 스키마(Pydantic)
class CountryDetail(BaseModel):
	country: str = Field(description="The name of the country")
	capital: str = Field(description="The capital city of the country")
	population: int = Field(description="The population of the country")
	language: str = Field(description="The official language of the country")
	currency: str = Field(description="The currency used in the country")

# LLM을 구조화 출력 모드로 래핑
structured_llm = llm.with_structured_output(CountryDetail)

# 프롬프트 템플릿 (명확한 JSON 필드 요구)
detail_prompt = PromptTemplate(
	template=(
		"""
		Give the following information about {country}:
		- Capital
		- Population (as an integer)
		- Official language
		- Currency
		
		Return ONLY a JSON object with exactly these fields:
		{{"country": "{country}", "capital": "...", "population": 0, "language": "...", "currency": "..."}}
		"""
	),
	input_variables=["country"],
)

# 테스트할 국가 목록
countries = ["France", "Japan", "Brazil", "India"]

for country in countries:
	print(f"\n=== {country} 정보 ===")
	messages = [
		SystemMessage(content="You are a helpful assistant that returns only valid JSON for the requested schema."),
		HumanMessage(content=detail_prompt.invoke({"country": country}).text),
	]
	# 구조화된 객체로 바로 응답 받기 (Pydantic 인스턴스)
	result: CountryDetail = structured_llm.invoke(messages)
	print("result: ", result)
	# 개별 필드 접근 예시
	print(f"Capital: {result.capital}")
	print(f"Population: {result.population:,}")
	print(f"Language: {result.language}")
	print(f"Currency: {result.currency}")
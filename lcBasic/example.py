from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="llama3.2:1b")

output_parser = StrOutputParser()

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

while True: 
    input_message = input("You : ")

    if input_message in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    chain = detail_prompt | llm | output_parser

    output = chain.invoke({"country": input_message})
    print("AI : ", output)
    

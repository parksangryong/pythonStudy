from langchain_ollama import ChatOllama

# llm = ChatOllama(model="deepseek-r1:1.5b")
llm = ChatOllama(model="llama3.2:1b")

result = llm.invoke("what is the capital of France?")

print(result.content)
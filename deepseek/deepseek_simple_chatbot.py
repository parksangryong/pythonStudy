from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = ChatOllama(model="deepseek-r1:7b")

messages = [
    SystemMessage(content="당신은 한국어로만 답변하는 AI입니다. 중국어나 다른 언어는 절대 사용하지 마세요. 모든 답변은 한국어로만 해주세요. <think> 태그나 사고 과정은 보여주지 말고 최종 답변만 출력하세요."),
]

while True:
    user_input = input("You\t: ").strip()

    if user_input in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=user_input))
    response = llm.stream(messages)
    
    ai_message = None
    for chunk in response:
        print(chunk.content, end="")
        if ai_message is None:
            ai_message = chunk
        else:
            ai_message += chunk
    print("")
    
    message_only = ai_message.content.split("</think>")[1].strip()
    messages.append(AIMessage(content=message_only))

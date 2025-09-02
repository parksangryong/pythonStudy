from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from tools.tools import get_current_time, get_yf_stock_history

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tools = [get_current_time, get_yf_stock_history]
tool_dict = {
    "get_current_time": get_current_time,
    "get_yf_stock_history": get_yf_stock_history
}

llm_with_tools = llm.bind_tools(tools)

messages = [
    SystemMessage(content="너는 사용자의 질문에 답변을 하기 위해 tools를 사용할 수 있다."),
    HumanMessage(content="부산의 현재 시간은 뭐야?")
]

messages.append(HumanMessage(content="테슬라는 한달 전에 비해 주가가 얼마나 올랐거나 내렸어?"))

response = llm_with_tools.invoke(messages)

for tool_call in response.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

# 마지막 메시지(도구 실행 결과)만 출력
print("=== 도구 실행 결과 ===")
print(messages[-1].content)

# 또는 전체 대화를 깔끔하게 보려면
print("\n=== 전체 대화 ===")
for i, msg in enumerate(messages):
    if hasattr(msg, 'content'):
        print(f"{i+1}. {type(msg).__name__}: {msg.content}")
    else:
        print(f"{i+1}. {type(msg).__name__}: {msg}")
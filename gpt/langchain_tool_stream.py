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

response = llm_with_tools.stream(messages)

is_first = True

for chunk in response:
    print("chunk type: ", type(chunk))
    if is_first:
        is_first = False
        gathered = chunk
    else:
        gathered += chunk

    print("content: ", gathered.content, "tool_call_chunk", gathered.tool_calls)

# AI의 tool_calls 메시지를 먼저 추가
messages.append(gathered)

# 도구 실행 결과를 ToolMessage로 생성하여 추가
for tool_call in gathered.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    result = selected_tool.invoke(tool_call["args"])
    
    # ToolMessage 생성 (tool_call_id 필수)
    from langchain_core.messages import ToolMessage
    tool_message = ToolMessage(
        content=result,
        tool_call_id=tool_call["id"]
    )
    messages.append(tool_message)

# 전체 대화 출력
print("\n=== 전체 대화 ===")
for i, msg in enumerate(messages):
    if hasattr(msg, 'content'):
        print(f"{i+1}. {type(msg).__name__}: {msg.content}")
    else:
        print(f"{i+1}. {type(msg).__name__}: {msg}")

# AI가 최종 답변 생성
final_response = llm_with_tools.invoke(messages)
print("\n=== AI 최종 답변 ===")
print(final_response.content)
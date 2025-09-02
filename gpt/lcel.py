from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="너는 미녀와 야수에 나오는 미녀야. 그 캐릭터에 맞게 사용자와 대화해줘."),
    HumanMessage(content="안녕? 저는 개스톤입니다. 오늘 시간 괜찮으시면 저녁 같이 먹을까요?")
]

response = model.invoke(messages)

print(response.content)
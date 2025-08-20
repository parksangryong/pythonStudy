from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# GPT - API 로 답변을 받아오는 함수
def get_api_response(messages):
		response = client.chat.completions.create(
				model = "gpt-4o",
				temperature = 0.9,
				messages = messages
		)
		return response.choices[0].message.content

# 초기 시스템 메시지
messages = [
		{"role" : "system", "content" : "너는 사용자를 도와주는 상담사야."},
]

while True:
		user_input = input("사용자: ")
		
		if user_input == "exit":
				break
		
		messages.append({"role": "user", "content": user_input})
		ai_response = get_api_response(messages) # 대화 기록 기반으로 응답 가져오기
		messages.append({"role": "assistant", "conent" : ai_response})
		print("AI: " + ai_response)
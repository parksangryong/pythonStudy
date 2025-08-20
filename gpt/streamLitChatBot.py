# 실행 : streamlit run streamLitChatBot.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# API 입력 해 따로 입력할 필요 없게함
with st.sidebar:
		openai_api_key = os.getenv("OPENAI_API_KEY")
		
st.title("📖 성경박사 AI")
st.markdown("---")

# 사용자의 세션 상태를 관리하는 기능 (메시지 없으면 초기 응답으로 설정)
if "messages" not in st.session_state:
		st.session_state["messages"] = [
			{"role": "system", "content": "당신은 성경박사입니다. 성경에 대한 깊은 지식과 이해를 바탕으로 성경 관련 질문에 답변해주세요. 성경 구절을 인용할 때는 정확한 장절을 명시하고, 역사적 배경과 문맥을 고려한 해석을 제공해주세요. 신학적 논의가 필요한 경우에는 다양한 관점을 제시하되, 성경 본문을 중심으로 한 해석을 우선시해주세요."},
			{"role": "assistant", "content": "안녕하세요! 저는 성경박사입니다. 성경에 대한 어떤 질문이든 도와드릴 수 있습니다. 구약, 신약, 특정 구절의 해석, 성경의 역사적 배경, 신학적 주제 등 무엇이든 물어보세요."}
		]
		
# 대화 기록을 웹에 출력하는 부분
for msg in st.session_state.messages:
		st.chat_message(msg["role"]).write(msg["content"])
		
# prompt 변수에 입력 담음 / 키 없으면 오류 반환
if prompt := st.chat_input():
		if not openai_api_key:
				st.info("Please add your OpenAI key to continue.")
				st.stop()
		
		# 질문을 세션에 저장 및 화면에 출력
		client = OpenAI(api_key = openai_api_key)
		st.session_state.messages.append({"role":"user", "content" : prompt})
		st.chat_message("user").write(prompt)
		
		# GPT 답변을 세션에 저장 및 화면에 출력
		response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
		msg = response.choices[0].message.content
		st.session_state.messages.append({"role": "assistant", "content" : msg})
		st.chat_message("assistant").write(msg)
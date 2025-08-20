# 실행 : streamlit run streamLitChatBot.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# API 입력 해 따로 입력할 필요 없게함
with st.sidebar:
		openai_api_key = os.getenv("OPENAI_API_KEY")
		
st.title("Chat BOt")

# 사용자의 세션 상태를 관리하는 기능 (메시지 없으면 초기 응답으로 설정)
if "messages" not in st.session_state:
		st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
		
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
		st.session_state.message.append({"role":"user", "content" : prompt})
		st.chat_message("user").write(prompt)
		
		# GPT 답변을 세션에 저장 및 화면에 출력
		response = client.chat.completions.create(model="gpt-4o", message=st.session_state.messages)
		msg = response.choices[0].message.content
		st.session_state.messages.append({"role": "assistant", "content" : msg})
		st.chat_message("assistant").write(msg)
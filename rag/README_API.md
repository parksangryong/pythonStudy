# RAG Chat API

Retrieval-Augmented Generation을 사용한 대화형 AI REST API 서버입니다.

## 🚀 주요 기능

- **자연스러운 대화**: 이전 대화 맥락을 기억하여 연속적인 대화 가능
- **질의 확장**: 모호한 질문을 명확하게 확장하여 정확한 답변 제공
- **세션 관리**: 여러 사용자의 대화를 독립적으로 관리
- **REST API**: FastAPI 기반의 표준 REST API 제공

## 📦 설치 및 실행

### 1. 패키지 설치

```bash
pip install -r requirements_api.txt
```

### 2. 환경변수 설정

`.env` 파일에 OpenAI API 키 설정:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 서버 실행

```bash
python rag_api.py
```

서버가 실행되면:

- API 문서: http://localhost:8000/docs
- 채팅 엔드포인트: POST http://localhost:8000/chat

## 🔧 API 사용법

### 기본 채팅

```python
import requests

# 채팅 요청
response = requests.post("http://localhost:8000/chat", json={
    "message": "서울시의 온실가스 저감 정책에 대해 알려줘",
    "use_query_expansion": True
})

result = response.json()
print(f"답변: {result['response']}")
```

### 세션을 유지한 연속 대화

```python
session_id = None

# 첫 번째 질문
response = requests.post("http://localhost:8000/chat", json={
    "message": "서울시의 환경 정책에 대해 알려줘",
    "session_id": session_id
})
result = response.json()
session_id = result["session_id"]

# 두 번째 질문 (이전 맥락 활용)
response = requests.post("http://localhost:8000/chat", json={
    "message": "그 정책의 비용은 얼마나 드나요?",
    "session_id": session_id
})
```

## 📋 API 엔드포인트

### POST /chat

채팅 메시지를 보내고 AI 응답을 받습니다.

**요청:**

```json
{
  "message": "질문 내용",
  "session_id": "세션 ID (선택사항)",
  "use_query_expansion": true
}
```

**응답:**

```json
{
  "session_id": "세션 ID",
  "message": "원본 질문",
  "response": "AI 답변",
  "expanded_query": "확장된 질문 (질의 확장 사용시)",
  "timestamp": "응답 시간"
}
```

### GET /sessions

활성 세션 목록을 조회합니다.

### GET /sessions/{session_id}/history

특정 세션의 대화 기록을 조회합니다.

### DELETE /sessions/{session_id}

세션을 삭제합니다.

### POST /sessions/{session_id}/clear

세션의 대화 기록을 초기화합니다.

## 🧪 테스트

### 자동 테스트 실행

```bash
python api_client_example.py
```

### 대화형 채팅 테스트

```bash
python api_client_example.py
# 선택: 2 (대화형 채팅)
```

## 💡 사용 예시

### 1. 명확한 질문

```
사용자: "서울시의 온실가스 저감 정책에 대해 알려줘"
AI: [서울시 정책에 대한 상세한 답변]
```

### 2. 모호한 질문 (질의 확장)

```
사용자: "뉴욕은?"
AI: [이전 대화 맥락을 고려하여 "뉴욕의 환경 정책"으로 확장하여 답변]
```

### 3. 맥락적 질문

```
사용자: "그 정책의 비용은 얼마나 드나요?"
AI: [이전에 언급된 정책의 비용에 대해 답변]
```

## 🔧 설정 옵션

- **질의 확장**: `use_query_expansion` 파라미터로 제어
- **검색 문서 수**: `retriever.as_retriever(k=3)`에서 k 값 조정
- **모델**: `ChatOpenAI` 모델 변경 가능
- **임베딩**: `OpenAIEmbeddings` 모델 변경 가능

## 🚨 주의사항

- 실제 운영환경에서는 세션 관리를 Redis나 데이터베이스로 변경 권장
- API 키 보안에 주의
- 벡터 데이터베이스가 미리 구축되어 있어야 함
- 메모리 사용량 모니터링 필요

## 📚 관련 파일

- `rag_api.py`: FastAPI 서버 메인 파일
- `api_client_example.py`: 클라이언트 사용 예시
- `requirements_api.txt`: 필요한 패키지 목록
- `rag_open_ai.py`: 원본 RAG 구현 (참고용)

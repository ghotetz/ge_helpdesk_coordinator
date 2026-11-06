# 📌 Google ADK Multi Agent Helpdesk Coordinator
> 사용자 문의를 코디네이터 에이전트가 분류해 IT, HR, GA 담당 하위 에이전트로 전달, 해결불가 건은 티켓 접수
> 
> 단일 거대 에이전트 대신 Google-ADK Sub-Agent 사용 예시 

## ⚡ 주요 기능 (Features)
> IT, HR(인사), GA(총무) 문의별 서브 에이전트로 호출

## 🛠 기술 스택 (Tech Stack)
- Google ADK, Python, Multi-Agent, Sub-Agents, Gemini-Enterprise, AI-Agents

## 💻 시작 가이드 (Getting Started)
- Google Cloud 인증
```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project ax-gemini-lab
```

- Google ADK 설치
```bash
python -m venv .venv && source .venv/bin/activate
pip install google-adk litellm
```

- ADK 검증
```bash
adk web
127.0.0.1:8000
```

- Agent 동작 확인
```bash
VPN 이 계속 끊겨요 > it_support 로 이동 및 해결 제공
재직증명서 발급 가능해요? > hr_support
2층 프린터 출력이 안돼요 > ga_support
```

- 검증 완료 후 Gemini Enterprise 에 에이전트로 등록
```bash
adk deploy agent_engine \
  --project="프로젝트명" \
  --region="리전명" \
  --display_name="에이전트명" \
  "에이전트 프로젝트 경로"
```

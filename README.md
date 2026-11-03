# 📌 Google ADK Helpdesk Agent
> 입사 연차 별 연차 일수 자동 계산 에이전트
> 
> Sub-Agent 사용 예시

## ⚡ 주요 기능 (Features)
> IT, HR(인사), GA(총무) 문의별 서브 에이전트로 호출

## 🛠 기술 스택 (Tech Stack)
- Google ADK, Python

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

- 검증 완료 후 Gemini Enterprise 에 에이전트로 등록
```bash
adk deploy agent_engine \
  --project="프로젝트명" \
  --region="리전명" \
  --display_name="에이전트명" \
  hr_policy_agent
```

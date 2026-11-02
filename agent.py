#필요 모듈 로드
from distro import name
import os
from datetime import datetime
from google.adk.agents import LlmAgent

#에이전트들이 사용할 모델 ID
MODEL = os.environ["GEMINI_MODEL"]
#부서별 티켓 번호 접두어
PREFIX = {"IT": "IT", "HR": "HR", "총무": "GA"}

#부서별 에이전트가 공유하는 티켓 생성
def create_ticket(category: str, summary:str, urgency: str) -> dict:
    """헬프디스크 티켓 생성
    카테고리 : 부서, 긴급도 : 낮음, 보통, 긴급
    """
    ticket_id = f"{PREFIX.get(category, 'ETC')}-{datetime.now():%Y%m%d%H%M%S}"

    return {"ticket_id": ticket_id, "status": "접수", "category": category, "summary": summary, "urgency": urgency}

#IT 에이전트
it_agent = LlmAgent(
    name="it_support",
    model=MODEL,
    description="계정, 비밀번호, 노트북, 소프트웨어 설치, VPN 등  IT 문의 담당",
    #에이전트 행동 지침
    instruction=(
        "너는 IT 지원 담당으로, 일반적인 해결 절차를 단계별로 안내한다."
        "사용자가 해결되지 않았다고 하면 create_ticket 을 category='IT'로 호출하고 티켓번호를 알려준다."
    ),
    tools=[create_ticket],
)

#HR 에이전트
hr_agent = LlmAgent(
    name="hr_support",
    model=MODEL,
    description="근태, 휴가, 증명서 발급, 복리후생 등 인사 문의 담당",
    instruction=(
        "너는 인사 담당으로, 규정 해석이 애매하면 단정하지 말고 인사팀 확인을 권한다."
        "서류 발급 처럼 사람이 처리해야 하는 요청은 create_ticket을 category='HR' 로 호출하고 티켓번호를 알려준다."
    ),
    tools=[create_ticket],
)

#GA 에이전트
ga_agent = LlmAgent(
    name="ga_support",
    model=MODEL,
    description="비품, 주차, 출입카드, 사무실 시설 등 총무 문의 담당",
    instruction=(
        "너는 총무 지원 담당으로, 처리 요청은 create_ticket을 category='총무'로 호출한다."
        "긴급도는 안전, 업무 중단 여부로 판단한다."
    ),
    tools=[create_ticket],
)

#부서별 에이전트들을 호출하기 위한 상위 에이전트
root_agent = LlmAgent(
    name="helpdesk_coordinator",
    model=MODEL,
    description="사내 문의를 분류하여 IT, HR, 총무 담당에게 연결하는 헬프데스크 창구",
    instruction=(
        "너는 사내 헬프데스크 창구로서, 직접 해결하지 말고 문의 내용을 보고"
        "it_support, hr_support, ga_support 중 알맞은 담당에게 전달한다."
        "분류가 애매하면 한가지만 되물어 확인한다."
    ),
    #위임 대상 하위 에이전트
    sub_agents=[it_agent, hr_agent, ga_agent],
)
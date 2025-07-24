import streamlit as st
import random

# 사전 정의된 데이터: 훅, 가치, CTA 템플릿 등
# 각 요소는 플레이스홀더를 포함하여 사용자 입력과 조합

HOOK_TEMPLATES = {
    "awareness": [
        "{topic}에 대해 {persona}이(가) 모르는 충격적 사실!",
        "상식 파괴: {topic}으로 {goal} 달성?",
        "내가 {persona}이었을 때 {topic}로 바뀐 인생"
    ],
    "interest": [
        "{topic}의 숨겨진 비밀 키워드 공개",
        "왜 {persona}은 {topic}을 해야 할까?",
        "실제 사례: {topic}으로 {goal} 성공 스토리"
    ],
    "desire": [
        "지금 {topic} 시작하면 {goal}이 현실이 된다",
        "{persona}을 위한 {topic} 로드맵",
        "이 {topic} 팁으로 {goal} 가까워지기"
    ],
    "action": [
        "{topic} 챌린지 참여하고 {goal} 쟁취!",
        "오늘 {topic} 적용하고 변화 느끼기",
        "프로필 링크에서 {goal} 관련 자료 받기"
    ]
}

VALUE_TEMPLATES = {
    "awareness": [
        "{persona}의 일상에 {topic}을 도입하는 간단한 방법 소개",
        "초보자도 이해하기 쉬운 {topic} 기본 개념 설명",
        "{topic}의 장점 3가지 나열"
    ],
    "interest": [
        "{topic} 실전 팁 1: {persona} 맞춤 적용법",
        "성공 사례 분석: 어떻게 {goal}을 달성했나",
        "{topic} 도구 추천과 사용법"
    ],
    "desire": [
        "상세 가이드: {topic}으로 {goal} 단계별 계획",
        "{persona}의 공감 포인트와 {topic} 솔루션",
        "미래 비전: {topic} 마스터하면 {goal} 달성"
    ],
    "action": [
        "즉시 실행 가능한 {topic} 액션 아이템",
        "{goal}을 위한 {topic} 챌린지 가이드",
        "독점 자료: {topic} 관련 다운로드 안내"
    ]
}

CTA_TEMPLATES = [
    "궁금하면 팔로우하고 더 알아보세요!",
    "댓글에 당신의 {topic} 경험 공유해요!",
    "프로필 링크에서 {goal} 관련 정보 확인!"
]

BGM_RECOMMENDATIONS = [
    "빠른 템포의 업비트 음악",
    "긴장감 있는 사운드트랙",
    "모티베이션 넘치는 BGM"
]

# AIDA 단계 정의
AIDA_STAGES = ["awareness", "interest", "desire", "action"]
AIDA_KR = {"awareness": "인지", "interest": "관심", "desire": "욕망", "action": "행동"}

# Streamlit UI
st.title("릴스 콘텐츠 전략 시스템")
st.subheader("백만 팔로워 목표를 위한 전략적 콘텐츠 생태계 구축")

# 사용자 입력
core_topic = st.text_input("핵심 주제 (core_topic)", placeholder="예: N잡으로 월 100만원 벌기")
target_persona = st.text_input("타겟 시청자 (target_persona)", placeholder="예: 회사 월급만으로 부족한 30대 직장인")
final_goal = st.text_input("최종 목표 (final_goal)", placeholder="예: 내 재테크 전자책 판매")

if st.button("콘텐츠 전략 생성"):
    if core_topic and target_persona and final_goal:
        # 시리즈 제목 생성
        series_title = f"{target_persona}을 위한 {core_topic}: {final_goal} 달성 챌린지"
        
        st.header("릴스 시리즈 제목")
        st.write(series_title)
        
        # AIDA 퍼널별 아이디어 생성
        ideas = {}
        for stage in AIDA_STAGES:
            ideas[stage] = []
            for i in range(3):
                hook = random.choice(HOOK_TEMPLATES[stage]).format(topic=core_topic, persona=target_persona, goal=final_goal)
                value = random.choice(VALUE_TEMPLATES[stage]).format(topic=core_topic, persona=target_persona, goal=final_goal)
                cta = random.choice(CTA_TEMPLATES).format(topic=core_topic, goal=final_goal)
                ideas[stage].append({"hook": hook, "value": value, "cta": cta})
        
        st.header("AIDA 퍼널별 릴스 아이디어")
        tabs = st.tabs([AIDA_KR[stage] for stage in AIDA_STAGES])
        
        for idx, stage in enumerate(AIDA_STAGES):
            with tabs[idx]:
                for i, idea in enumerate(ideas[stage], 1):
                    with st.expander(f"아이디어 #{i}"):
                        st.write(f"**훅:** {idea['hook']}")
                        st.write(f"**가치:** {idea['value']}")
                        st.write(f"**CTA:** {idea['cta']}")
        
        # 킬러 콘텐츠 스크립트: 관심 단계의 첫 번째 아이디어 선택
        killer_idea = ideas["interest"][0]
        st.header("킬러 콘텐츠 스크립트 (관심 단계 첫 아이디어)")
        script = f"""
(장면#1 - 1초): ({random.choice(BGM_RECOMMENDATIONS)}) "{killer_idea['hook']}" 라는 자막과 함께 충격적 이미지 표시.

(장면#2 - 5-10초): (화면 전환) "{killer_idea['value']}" 라는 자막과 함께, 단계별 설명 및 시각 자료 제시.

(장면#3 - 2초): "{killer_idea['cta']}" 라는 자막과 함께 행동 유도 버튼 또는 링크 강조.
"""
        st.write(script)
        
        # 주간 발행 캘린더
        calendar = [
            ("월요일", "인지 릴스 #1 (새로운 잠재고객 유입)"),
            ("화요일", "인지 릴스 #2"),
            ("수요일", "관심 릴스 #1 (전문성으로 신뢰 구축)"),
            ("목요일", "관심 릴스 #2"),
            ("금요일", "욕망 릴스 #1 (주말 구매 심리 자극)"),
            ("토요일", "행동 릴스 #1 (즉시 행동 유도)"),
            ("일요일", "욕망 릴스 #2 (휴식 중 반성 유도)")
        ]
        # 12개 아이디어를 분배하기 위해 확장 (예시로 7일, 반복 가능)
        st.header("주간 발행 캘린더")
        for day, desc in calendar:
            st.write(f"**{day}:** {desc}")
        
    else:
        st.error("모든 입력 항목을 채워주세요.")

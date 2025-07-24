import streamlit as st
import pandas as pd
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="릴스 콘텐츠 전략 시스템",
    page_icon="👑",
    layout="wide"
)

# --- 전문가 데이터베이스 (내부 데이터) ---
# 이 데이터베이스는 검증된 마케팅 프레임워크를 기반으로 합니다.

# 1. 훅(Hook) 템플릿: 심리적 트리거 기반
HOOKS = {
    "상식 파괴": [
        "아직도 {topic}을(를) 이렇게 하고 계신가요?",
        "{topic}에 대한 가장 큰 오해 3가지",
        "사실 {topic}은(는) OOO이 아닙니다.",
        "당신이 {topic}에 실패하는 진짜 이유, 아무도 말해주지 않았을 겁니다."
    ],
    "비밀/희소성": [
        "상위 1%만 아는 {topic} 비밀",
        "저만 알고 싶었던 {topic} 꿀팁 대방출",
        "이건 진짜 아는 사람만 돈 버는 {topic} 정보입니다.",
        "업계 비밀인데, {topic}의 핵심은 사실 OOO입니다."
    ],
    "개인적 고백/경험": [
        "제가 {topic} 때문에 1,000만원 날리고 깨달은 것",
        "평범한 {persona}이었던 제가 {topic}으로 인생 역전한 썰",
        "솔직히 말할게요. {topic} 처음 시작했을 때...",
        "이건 제 실패담입니다. {topic}할 때 절대 OOO은 하지 마세요."
    ],
    "질문/자가진단": [
        "당신의 {topic} 수준은? (1분 자가진단 테스트)",
        "혹시 당신도 {topic}할 때 이런 실수하고 있나요?",
        "단 1가지만 질문할게요. {topic}, 자신 있으신가요?",
        "{topic} 시작하기 전, 이것부터 체크해보세요."
    ]
}

# 2. 가치(Value) 템플릿: 시청자가 저장하게 만드는 정보
VALUES = {
    "실용적 팁": [
        "딱 3가지만 기억하세요. 첫째, OOO. 둘째, OOO...",
        "가장 빠르고 쉬운 {topic} 방법 A, B, C",
        "초보자도 바로 써먹는 {topic} 공식",
        "시간과 돈을 아껴주는 {topic} 치트키"
    ],
    "깊은 공감": [
        "사실 우리 모두 {topic} 앞에서 작아지곤 하죠. 하지만 괜찮아요.",
        "{persona}이라면 누구나 공감할 {topic}의 어려움",
        "OOO 때문에 힘드셨죠? 그 마음 제가 가장 잘 압니다.",
        "이 영상을 보는 당신도 할 수 있다는 걸 보여주고 싶었어요."
    ],
    "새로운 관점": [
        "문제를 다르게 보세요. {topic}의 핵심은 OOO이 아니라 OOO입니다.",
        "남들과 똑같이 해서는 {topic}에서 절대 성공할 수 없습니다.",
        "데이터로 증명된 {topic}의 놀라운 효과",
        "{topic}을(를) OOO와 연결하면 엄청난 시너지가 납니다."
    ]
}

# 3. CTA(Call To Action) 템플릿: 퍼널 단계별 행동 유도
CTAS = {
    "Awareness": [
        "더 많은 {topic} 꿀팁이 궁금하다면 지금 바로 팔로우!",
        "매일 유용한 {topic} 정보를 받아보세요. (팔로우 필수)",
        "이 시리즈가 기대된다면 '🔥' 이모지를 남겨주세요!"
    ],
    "Interest": [
        "자세한 내용은 댓글에 남겨둘게요!",
        "가장 중요한 OOO은 프로필 링크에서 확인하세요!",
        "여러분은 어떻게 생각하세요? 댓글로 의견을 나눠주세요."
    ],
    "Desire": [
        "곧 {topic} 관련 라이브 방송을 할 예정이니 알림 설정!",
        "선착순 100명에게만 드리는 {topic} 무료 가이드북, 프로필 링크 확인!",
        "이 모든 노하우가 담긴 {final_goal}이(가) 궁금하다면 DM 주세요."
    ],
    "Action": [
        "마감이 얼마 남지 않았어요! 지금 바로 {final_goal} 신청하기 (프로필 링크)",
        "DM으로 '신청'이라고 보내주시면 선착순으로 마감됩니다.",
        "더 이상 고민하지 마세요. 당신의 인생을 바꿀 기회입니다. (프로필 링크)"
    ]
}

# 4. 킬러 스크립트 BGM 추천
BGM_SUGGESTIONS = [
    "Upbeat, energetic pop song (e.g., 'Good Parts' by LE SSERAFIM)",
    "Mysterious, curiosity-inducing cinematic music",
    "Fast-paced, motivational electronic track",
    "Calm, trustworthy lo-fi hip hop beat"
]

# --- 함수 정의 ---
def generate_idea(stage, topic, persona, goal):
    """AIDA 퍼널 단계별로 훅-가치-CTA 아이디어를 생성하는 함수"""
    hook_type = random.choice(list(HOOKS.keys()))
    hook = random.choice(HOOKS[hook_type]).format(topic=topic, persona=persona)
    
    value_type = random.choice(list(VALUES.keys()))
    value = random.choice(VALUES[value_type]).format(topic=topic, persona=persona)
    
    cta = random.choice(CTAS[stage]).format(topic=topic, final_goal=goal)
    
    return {"hook": hook, "value": value, "cta": cta}

# --- Streamlit UI ---
st.title("👑 백만 팔로워 릴스 콘텐츠 전략 시스템")
st.markdown("---")
st.info("**단 3가지만 입력하면, 검증된 마케팅 프레임워크에 기반한 '릴스 콘텐츠 생태계'를 자동으로 구축합니다.**")

with st.form("strategy_form"):
    st.header("Step 1: 당신의 비즈니스 정보 입력")
    core_topic = st.text_input("1. 릴스의 핵심 주제는 무엇인가요?", placeholder="예: N잡으로 월 100만원 벌기")
    target_persona = st.text_input("2. 누구를 위한 콘텐츠인가요? (타겟 시청자)", placeholder="예: 회사 월급만으로 부족한 30대 직장인")
    final_goal = st.text_input("3. 이 콘텐츠 시리즈의 최종 목표는 무엇인가요?", placeholder="예: 내 재테크 전자책 판매")
    
    submit_button = st.form_submit_button("🚀 전략 시스템 구축 시작")

if submit_button:
    if not all([core_topic, target_persona, final_goal]):
        st.error("🚨 모든 항목을 입력해야 정확한 전략 시스템을 구축할 수 있습니다.")
    else:
        st.success("📈 시스템 구축이 완료되었습니다! 아래에서 당신만의 완벽한 콘텐츠 퍼널을 확인하세요.")
        st.markdown("---")

        # 1. 릴스 시리즈 제목 생성
        series_title = f"평범한 {target_persona}을(를) 위한 '{core_topic}' 완전 정복 챌린지"
        st.header("🎬 릴스 시리즈 전체 컨셉")
        st.subheader(f"시리즈 제목: {series_title}")
        st.write(f"**이 시리즈의 목표:** 단순 정보 나열이 아닌, {target_persona}의 문제를 해결하고 최종적으로 '{final_goal}'까지 자연스럽게 연결되는 콘텐츠 여정을 설계합니다.")
        st.markdown("---")

        # 2. AIDA 퍼널별 아이디어 생성 및 출력
        st.header("♟️ AIDA 퍼널 기반 콘텐츠 아이디어 (총 12개)")
        
        # 아이디어 생성
        ideas = {
            "Awareness": [generate_idea("Awareness", core_topic, target_persona, final_goal) for _ in range(3)],
            "Interest": [generate_idea("Interest", core_topic, target_persona, final_goal) for _ in range(3)],
            "Desire": [generate_idea("Desire", core_topic, target_persona, final_goal) for _ in range(3)],
            "Action": [generate_idea("Action", core_topic, target_persona, final_goal) for _ in range(3)]
        }
        
        # 탭으로 출력
        tabs = st.tabs(["**1단계: 인지 (Awareness)**", "**2단계: 관심 (Interest)**", "**3단계: 욕망 (Desire)**", "**4단계: 행동 (Action)**"])
        
        for i, stage in enumerate(ideas.keys()):
            with tabs[i]:
                st.subheader(f"🎯 목표: 잠재고객의 스크롤을 멈추고 내 존재를 각인시키기")
                for j, idea in enumerate(ideas[stage]):
                    with st.expander(f"**아이디어 #{j+1}**"):
                        st.markdown(f"**🔥 Hook (1초):** {idea['hook']}")
                        st.markdown(f"**💎 Value (5-10초):** {idea['value']}")
                        st.markdown(f"**👉 CTA (2초):** {idea['cta']}")
        
        st.markdown("---")

        # 3. 킬러 콘텐츠 스크립트 생성
        st.header("🔥 10만 조회수 '킬러 콘텐츠' 상세 스크립트")
        st.write("**'관심(Interest)' 단계의 아이디어를 기반으로, 시청자의 저장과 공유를 유발하는 상세 스크립트 예시입니다.**")
        
        killer_idea = ideas["Interest"][0]
        
        st.code(f"""
        [릴스 상세 스크립트 예시]

        - **타겟:** {target_persona}
        - **주제:** {core_topic}
        - **BGM 추천:** {random.choice(BGM_SUGGESTIONS)}

        ---

        **[장면 #1: 0-2초]**
        - **화면:** (강렬한 타이포그래피) "{killer_idea['hook']}"
        - **자막:** 화면과 동일
        - **효과음:** 'Whoosh' 또는 'Ding' 효과음으로 주목 끌기

        **[장면 #2: 2-7초]**
        - **화면:** 당신이 직접 나와서, {killer_idea['value']}의 핵심 내용을 손가락으로 짚거나, 관련 자료를 보여주며 설명하는 장면. (빠른 화면 전환)
        - **자막:** 핵심 내용 1, 2, 3을 간결하게 요약해서 보여줌. (예: 1. OOO 하기 2. OOO 절대 금지)
        - **내레이션(선택):** "많은 분들이 OOO을 놓치고 있어요. 하지만 진짜 중요한 건..."

        **[장면 #3: 7-9초]**
        - **화면:** 마지막으로 강조하고 싶은 메시지나, 결과물을 보여주는 장면. (예: Before/After 이미지)
        - **자막:** "{killer_idea['cta']}"
        - **효과:** 시청자가 행동할 수 있도록 프로필 링크나 댓글 창을 가리키는 화살표 애니메이션 추가.
        """, language='markdown')

        st.markdown("---")

        # 4. 주간 발행 캘린더 생성
        st.header("🗓️ 전략적 주간 발행 캘린더")
        st.write("**콘텐츠 퍼널 효과를 극대화하기 위한 추천 발행 순서입니다.**")

        calendar_data = {
            "요일": ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일"],
            "AIDA 단계": ["Awareness", "Interest", "Awareness", "Interest", "Desire", "Action"],
            "콘텐츠 아이디어": [
                "인지 아이디어 #1", 
                "관심 아이디어 #1", 
                "인지 아이디어 #2", 
                "관심 아이디어 #2",
                "욕망 아이디어 #1",
                "행동 아이디어 #1"
            ],
            "전략적 목표": [
                "새로운 잠재고객 유입", 
                "전문성으로 신뢰 구축", 
                "도달률 극대화", 
                "깊은 공감대 형성",
                "구매 욕구 자극",
                "주말 매출 전환 유도"
            ]
        }
        df = pd.DataFrame(calendar_data)
        st.table(df)

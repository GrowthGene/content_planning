import streamlit as st
import pandas as pd
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="콘텐츠 기둥 전략 시스템",
    page_icon="🏛️",
    layout="wide"
)

# --- 전문가 데이터베이스 (콘텐츠 기둥 방법론 기반) ---
# 시중 코칭 프로그램(Hootsuite, Evercoach)의 핵심 전략을 분석하여 구성

# 1. 콘텐츠 포맷 템플릿
CONTENT_FORMATS = [
    "릴스: 15초 데모",
    "카드뉴스: 인포그래픽",
    "포스트: 시리즈 글",
    "스토리: Q&A/투표"
]

# 2. 바이럴 앵글 템플릿 (조회수 50만+ 포텐셜)
VIRAL_ANGLES = {
    "변신 팁": [
        "'Before & After' 극적인 변화 과정 공개",
        "초보자가 가장 많이 하는 실수 Top 3",
        "단 1가지 교정으로 얻는 놀라운 효과",
        "시간/비용을 1/10로 줄이는 치트키"
    ],
    "나의 여정": [
        "가장 힘들었던 순간과 극복기 (취약점 고백)",
        "수백만 원 쓰고 깨달은 진짜 노하우",
        "나의 부끄러운 실패담 최초 공개",
        "평범했던 내가 전문가가 되기까지의 과정"
    ],
    "액션 챌린지": [
        "함께하는 '7일 챌린지' 시작 공지",
        "미션 참여 독려 및 중간 점검",
        "챌린지 성공 시 얻게 될 보상 공개",
        "참가자들의 놀라운 성공 사례 공유"
    ]
}

# --- 함수 정의 ---
def generate_mindmap_ideas(pillar_name, pillar_type):
    """콘텐츠 기둥별로 20개의 마인드맵 아이디어를 생성하는 함수"""
    if not pillar_name or not pillar_type:
        return []
        
    ideas = []
    angles = VIRAL_ANGLES.get(pillar_type, VIRAL_ANGLES["변신 팁"]) # 기본값 설정
    
    for _ in range(20):
        # 다양한 포맷과 앵글을 조합하여 아이디어 생성
        content_format = random.choice(CONTENT_FORMATS)
        angle = random.choice(angles)
        idea_text = f"{content_format} - '{pillar_name}' 관련 {angle}"
        # Hootsuite BGM 추천과 같은 부가 정보 추가
        if "릴스" in content_format or "스토리" in content_format:
            idea_text += " (Tip: 인기 BGM 활용)"
        ideas.append(idea_text)
    return ideas

# --- Streamlit UI ---
st.title("🏛️ 콘텐츠 기둥 기반 전략 시스템 (v4.0)")
st.info("**시중 유료 코칭의 핵심 방법론을 담았습니다. 3개의 '콘텐츠 기둥'을 정의하여, 당신만의 강력한 콘텐츠 시스템을 구축하세요.**")

with st.form("pillar_form"):
    st.header("Step 1: 당신의 핵심 콘텐츠 기둥(Pillar) 정의")
    
    col1, col2 = st.columns(2)
    with col1:
        pillar1_name = st.text_input("1. 첫 번째 콘텐츠 기둥의 주제는 무엇인가요?", placeholder="예: 뱃살 다이어트")
        pillar2_name = st.text_input("2. 두 번째 콘텐츠 기둥의 주제는 무엇인가요?", placeholder="예: 건강한 식단")
        pillar3_name = st.text_input("3. 세 번째 콘텐츠 기둥의 주제는 무엇인가요?", placeholder="예: 홈트레이닝 챌린지")
    with col2:
        pillar1_type = st.selectbox("기둥 1의 성격 선택", options=VIRAL_ANGLES.keys(), key="p1_type", help="어떤 종류의 이야기를 주로 다룰지 선택하세요.")
        pillar2_type = st.selectbox("기둥 2의 성격 선택", options=VIRAL_ANGLES.keys(), key="p2_type")
        pillar3_type = st.selectbox("기둥 3의 성격 선택", options=VIRAL_ANGLES.keys(), key="p3_type")

    submit_button = st.form_submit_button("🚀 콘텐츠 시스템 구축")

if submit_button:
    if not all([pillar1_name, pillar2_name, pillar3_name]):
        st.error("🚨 3개의 콘텐츠 기둥 주제를 모두 입력해야 합니다.")
    else:
        st.success("📈 시스템 구축이 완료되었습니다! 아래에서 당신의 강력한 콘텐츠 자산을 확인하세요.")
        st.markdown("---")

        pillars = {
            pillar1_name: pillar1_type,
            pillar2_name: pillar2_type,
            pillar3_name: pillar3_type
        }

        # 1. 마인드맵 아이디어 생성 및 출력
        st.header("🧠 50만 조회수 포텐셜, 콘텐츠 아이디어 마인드맵 (총 60개)")
        
        for pillar_name, pillar_type in pillars.items():
            with st.expander(f"**기둥: {pillar_name} (성격: {pillar_type}) - 아이디어 20개 펼쳐보기**"):
                ideas = generate_mindmap_ideas(pillar_name, pillar_type)
                if ideas:
                    # 보기 좋게 2열로 표시
                    col1, col2 = st.columns(2)
                    for i, idea in enumerate(ideas):
                        if i < 10:
                            col1.write(f"💡 Idea {i+1}: {idea}")
                        else:
                            col2.write(f"💡 Idea {i+1}: {idea}")
                else:
                    st.write("아이디어를 생성할 수 없습니다. 기둥 정보를 확인해주세요.")
        
        st.markdown("---")

        # 2. 주간 콘텐츠 캘린더 생성
        st.header("🗓️ 전략적 주간 콘텐츠 캘린더")
        st.write("**'초기-중기-수익화' 단계를 고려하여 콘텐츠를 전략적으로 배분한 Hootsuite 스타일 템플릿입니다.**")

        calendar_data = {
            "요일": ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일"],
            "콘텐츠 기둥": [
                pillar1_name, 
                pillar2_name, 
                pillar1_name, 
                pillar3_name,
                pillar2_name,
                pillar3_name,
            ],
            "콘텐츠 포맷": ["릴스", "카드뉴스", "스토리", "릴스", "포스트", "스토리(CTA)"],
            "전략적 목표": [
                "**초창기:** 기본 팁으로 신규 팔로워 유입", 
                "**초창기:** 정보성 콘텐츠로 전문성 각인", 
                "**중간:** 소통/Q&A로 커뮤니티 활성화", 
                "**중간:** 챌린지로 참여 및 바이럴 유도",
                "**수익화:** 고객 성공사례로 신뢰도 증폭",
                "**수익화:** 제품/서비스 구매 전환 (강력한 CTA)"
            ]
        }
        df = pd.DataFrame(calendar_data)
        st.table(df)
        
        st.info("""
        **💡 캘린더 활용법:**
        - **월/화:** 새로운 잠재고객을 끌어들이는 데 집중하세요. (넓은 주제, 쉬운 팁)
        - **수/목:** 기존 팔로워의 참여를 유도하고 관계를 깊게 만드세요. (챌린지, 소통)
        - **금/토:** 구축된 신뢰를 바탕으로 자연스럽게 수익 창출 기회를 만드세요. (주말 프로모션)
        """)

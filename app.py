import streamlit as st
import pandas as pd
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="1:1 프리미엄 콘텐츠 코칭 시스템",
    page_icon="👑",
    layout="wide"
)

# --- 전문가 데이터베이스 (최상위 코칭 프레임워크 기반) ---

# 1. 콘텐츠 아이디어 생성 프레임워크
FRAMEWORKS = {
    "나의 여정": {
        "name": "영웅의 여정 (Hero's Journey)",
        "angles": [
            "[소명] 내가 왜 이 일을 시작하게 되었는가",
            "[시련] 가장 큰 위기와 그것을 극복한 과정",
            "[깨달음] 실패를 통해 얻은 결정적인 교훈",
            "[귀환] 이제 사람들에게 어떤 도움을 주고 싶은가"
        ]
    },
    "변신 팁": {
        "name": "PAS (Problem-Agitate-Solve)",
        "angles": [
            "[문제정의] 고객이 겪는 명확한 문제점 지적하기",
            "[문제악화] 이 문제를 방치했을 때 벌어지는 최악의 상황",
            "[해결책] 문제를 해결할 수 있는 나의 구체적인 방법 제시",
            "[결과증명] 내 방법으로 성공한 고객의 실제 사례"
        ]
    },
    "액션 챌린지": {
        "name": "커뮤니티 빌딩 (Community Building)",
        "angles": [
            "[동기부여] 우리가 왜 함께 이 도전을 해야 하는가",
            "[미션제시] 이번 주 함께 달성할 구체적인 미션",
            "[참여독려] 참여자들의 과정을 공유하고 응원하기",
            "[성취보상] 챌린지를 완수한 사람들에게 주어지는 혜택"
        ]
    }
}

# 2. 콘텐츠 포맷 및 BGM
CONTENT_FORMATS = ["릴스", "카드뉴스", "시리즈 포스트", "라이브 방송", "스토리 Q&A"]
BGM_SUGGESTIONS = ["감성적인 피아노 BGM", "빠른 비트의 동기부여 팝송", "신뢰감을 주는 뉴스 스타일의 BGM", "궁금증을 유발하는 미스터리한 사운드"]

# --- 함수 정의 ---

def generate_premium_ideas(pillar_name, pillar_type, brand_mission, audience_pain, audience_dream):
    """프리미엄 코칭 내용을 담은 콘텐츠 브리프를 생성하는 함수"""
    if not all([pillar_name, pillar_type, brand_mission, audience_pain, audience_dream]):
        return []
    
    ideas = []
    framework = FRAMEWORKS.get(pillar_type)
    if not framework:
        return []

    for angle in framework["angles"]:
        brief = {
            "title": f"[{pillar_name}] {angle}",
            "format": random.choice(CONTENT_FORMATS),
            "core_message": f"'{audience_pain}'을 겪는 고객이 '{audience_dream}'을 이룰 수 있도록, '{brand_mission}'의 관점에서 이 이야기를 전달합니다.",
            "strategic_angle": f"이 콘텐츠는 고객의 문제({audience_pain})를 직접 건드려 공감대를 형성하고, 해결책을 통해 당신의 전문성을 증명합니다. ({framework['name']} 프레임워크 활용)",
            "cta": "더 깊은 이야기가 궁금하다면, 댓글로 질문을 남겨주세요."
        }
        ideas.append(brief)
    return ideas

# --- Streamlit UI ---
st.title("👑 100만 원 가치의 1:1 코칭 시스템 (v5.0)")
st.info("**실제 프리미엄 코칭 세션의 질문에 답변하고, 당신의 비즈니스를 성장시킬 '전략적 콘텐츠 시스템'을 구축하세요.**")

with st.form("coaching_form"):
    st.header("Step 1: 심층 진단 (1:1 코칭 세션)")
    
    with st.expander("**Part 1: 당신의 브랜드 정체성(WHY)은 무엇인가요?**", expanded=True):
        brand_mission = st.text_area("1. 당신이 이 일을 통해 세상에 어떤 긍정적 변화를 만들고 싶나요? (브랜드 미션)", placeholder="예: 모든 여성이 타인의 시선에서 벗어나 온전한 자신의 아름다움을 찾고 사랑하게 만든다.")
        unique_value_prop = st.text_area("2. 다른 사람이 아닌, '오직 당신만'이 줄 수 있는 독창적인 가치는 무엇인가요?", placeholder="예: 10년간의 운동 코칭 경험과 심리학을 접목한 '마음챙김 바디 프로필' 프로그램을 제공합니다.")

    with st.expander("**Part 2: 당신의 고객은 누구인가요?**", expanded=True):
        audience_pain = st.text_input("3. 고객이 밤에 잠 못 이루게 만드는 가장 큰 고통/두려움은 무엇인가요?", placeholder="예: 출산 후 망가진 몸을 보며 평생 이렇게 살게 될까 봐 두렵다.")
        audience_dream = st.text_input("4. 고객이 궁극적으로 원하는 꿈, 이상적인 모습은 무엇인가요?", placeholder="예: '애 엄마'가 아닌, 자신감 넘치는 여성으로서의 나를 되찾고 싶다.")

    with st.expander("**Part 3: 고객을 도울 3개의 콘텐츠 기둥(Pillar)은 무엇인가요?**", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            pillar1_name = st.text_input("콘텐츠 기둥 1 주제", placeholder="예: 출산 후 다이어트")
            pillar2_name = st.text_input("콘텐츠 기둥 2 주제", placeholder="예: 나의 실패와 성공기")
            pillar3_name = st.text_input("콘텐츠 기둥 3 주제", placeholder="예: 30일 바디프로필 챌린지")
        with col2:
            pillar1_type = st.selectbox("기둥 1 성격", options=FRAMEWORKS.keys(), key="p1")
            pillar2_type = st.selectbox("기둥 2 성격", options=FRAMEWORKS.keys(), key="p2")
            pillar3_type = st.selectbox("기둥 3 성격", options=FRAMEWORKS.keys(), key="p3")

    submit_button = st.form_submit_button("🚀 100만 원 가치의 컨설팅 결과 받기")

if submit_button:
    if not all([brand_mission, unique_value_prop, audience_pain, audience_dream, pillar1_name, pillar2_name, pillar3_name]):
        st.error("🚨 모든 심층 진단 질문에 답변해야 100만 원 가치의 컨설팅이 가능합니다.")
    else:
        st.success("📈 컨설팅이 완료되었습니다. 이것이 당신의 비즈니스를 성장시킬 청사진입니다.")
        st.markdown("---")

        # 1. 브랜드 전략 요약
        st.header("📜 당신의 브랜드 전략 청사진")
        st.markdown(f"""
        - **브랜드 미션 (WHY):** {brand_mission}
        - **독창적 가치 (HOW):** {unique_value_prop}
        - **타겟 고객:** '{audience_pain}'이라는 고통을 겪고 있으며, '{audience_dream}'을 꿈꾸는 사람
        - **솔루션:** 3개의 콘텐츠 기둥(**{pillar1_name}, {pillar2_name}, {pillar3_name}**)을 통해 고객을 이상적인 모습으로 이끈다.
        """)
        st.markdown("---")

        # 2. 4주 콘텐츠 시스템 생성
        st.header("🗓️ 잠재고객을 팬으로 만드는 4주 콘텐츠 시스템")
        
        # 아이디어 풀 생성
        all_ideas = []
        pillars = {pillar1_name: pillar1_type, pillar2_name: pillar2_type, pillar3_name: pillar3_type}
        for name, p_type in pillars.items():
            all_ideas.extend(generate_premium_ideas(name, p_type, brand_mission, audience_pain, audience_dream))
        
        random.shuffle(all_ideas)
        
        week_themes = {
            "Week 1: 인지 & 공감": "고객의 고통에 깊이 공감하며 당신의 존재를 알리는 주",
            "Week 2: 교육 & 권한 부여": "실질적인 해결책을 제공하여 전문가로서 신뢰를 쌓는 주",
            "Week 3: 참여 & 커뮤니티": "고객의 참여를 유도하고 소속감을 느끼게 하는 주",
            "Week 4: 영감 & 전환": "성공 사례를 보여주고 자연스럽게 다음 단계로 이끄는 주"
        }
        
        idea_idx = 0
        for week, desc in week_themes.items():
            with st.expander(f"**{week} - {desc}**", expanded=(week=="Week 1: 인지 & 공감")):
                for day in ["월", "수", "금"]:
                    if idea_idx < len(all_ideas):
                        idea = all_ideas[idea_idx]
                        st.subheader(f"📌 {day}요일 콘텐츠 브리프: {idea['title']}")
                        st.markdown(f" - **추천 포맷:** `{idea['format']}`")
                        st.markdown(f" - **핵심 메시지:** {idea['core_message']}")
                        st.markdown(f" - **전략적 의도:** {idea['strategic_angle']}")
                        st.markdown(f" - **Call to Action:** `{idea['cta']}`")
                        st.divider()
                        idea_idx += 1
        
        st.markdown("---")

        # 3. 킬러 콘텐츠 상세 스크립트
        st.header("🔥 50만 조회수를 위한 '킬러 콘텐츠' 상세 스크립트")
        st.write("Week 2의 교육 콘텐츠를 기반으로, 시청자가 저장하고 공유할 수밖에 없는 릴스 스크립트 예시입니다.")
        
        killer_idea = next((idea for idea in all_ideas if "해결책" in idea['title']), all_ideas[4] if len(all_ideas)>4 else all_ideas[0])

        # SyntaxError가 발생했던 st.code 블록을 깨끗한 코드로 수정합니다.
        st.code(f"""
[릴스 상세 스크립트: {killer_idea['title']}]

- **BGM 추천:** {random.choice(BGM_SUGGESTIONS)}

---

**[SCENE #1: 0-2초 / HOOK]**
- (화면) '{audience_pain}'이라는 자막이 화면을 크게 채운다.
- (자막) 당신도 이 문제 때문에 힘드신가요?
- (효과) 문제점을 상징하는 흑백 이미지 또는 영상

**[SCENE #2: 2-8초 / AGITATE & SOLVE]**
- (화면) 당신이 직접 등장하여, 문제의 핵심 원인을 손가락으로 짚으며 설명.
- (자막) 하지만 진짜 원인은 OOO입니다. 해결책은 바로 이것입니다. (해결책 키워드 강조)
- (내레이션) "많은 분들이 OOO만 해결하면 된다고 착각해요. 하지만 진짜 문제는 OOO입니다. 제가 알려드리는 이 방법 하나면..."

**[SCENE #3: 8-13초 / VALUE & PROOF]**
- (화면) 해결책을 적용하는 구체적인 방법을 시연. (Before/After 화면을 빠르게 교차 편집)
- (자막) 1. OOO 하기 / 2. OOO 하기 / 3. OOO 하기 -> 결과 확인!
- (효과) 성공적인 결과 화면에서 밝고 긍정적인 효과(빛, 반짝임) 추가

**[SCENE #4: 13-15초 / CTA]**
- (화면) 당신이 웃으며 시청자를 바라보는 모습.
- (자막) 이 방법이 도움이 되셨다면 '저장'하시고, 더 궁금한 점은 댓글로 남겨주세요!
""", language='markdown')


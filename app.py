import streamlit as st
import random

st.title("SNS 콘텐츠 기획 프로그램")
st.write("시중 코치 방법 기반: 콘텐츠 기둥 정의 → 아이디어 생성 → 캘린더 (e.g., Hootsuite 템플릿, Evercoach pillars)")

# 입력: 기둥 정의
pillar1 = st.text_input("콘텐츠 기둥 1 (e.g., '변신 팁'):", "")
pillar2 = st.text_input("콘텐츠 기둥 2 (e.g., '나의 여정'):", "")
pillar3 = st.text_input("콘텐츠 기둥 3 (e.g., '액션 챌린지'):", "")

if st.button("콘텐츠 아이디어 생성"):
    if all([pillar1, pillar2, pillar3]):
        # 조회수 높은 아이디어 생성
        formats = ["릴스: 15초 데모", "카드뉴스: 인포그래픽", "스토리: 폴 상호작용", "포스트: Before-After"]
        for pillar in [pillar1, pillar2, pillar3]:
            st.subheader(f"[마인드맵: {pillar} (20 아이디어, 조회수 50만+ 포텐셜: viral hooks like vulnerability)]")
            for i in range(20):
                fmt = random.choice(formats)
                idea = f"Idea {i+1}: {fmt} - {pillar} 관련 '{random.choice(['Before-After', 'Quick Tip', 'Challenge', 'Story Share'])}' (e.g., Hootsuite BGM 추가)."
                st.write(idea)
        
        # 캘린더
        st.subheader("[주간 콘텐츠 캘린더 플랜]")
        st.write(f"월: {pillar1} 릴스 (초창기: 기본 팁)")
        st.write(f"화: {pillar2} 스토리 (중간: 여정 repurposing)")
        st.write(f"수: {pillar3} 챌린지 (수익화: 제품 링크 CTA, MeetEdgar 스타일)")
    else:
        st.error("모든 기둥을 입력해주세요.")
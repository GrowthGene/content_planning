import random

def content_planning():
    print("=== SNS 컨텐츠 기획 프로그램 ===")
    print("시중 코치 방법 기반: 콘텐츠 기둥 정의 → 아이디어 생성 → 캘린더 (e.g., Hootsuite 템플릿, Evercoach pillars)")
    
    # 입력: 기둥 정의
    pillar1 = input("콘텐츠 기둥 1 (e.g., '변신 팁'): ")
    pillar2 = input("콘텐츠 기둥 2 (e.g., '나의 여정'): ")
    pillar3 = input("콘텐츠 기둥 3 (e.g., '액션 챌린지'): ")
    
    # 조회수 높은 아이디어 생성 (랜덤 믹스 for variety, TikTok 스타일: short, engaging)
    formats = ["릴스: 15초 데모", "카드뉴스: 인포그래픽", "스토리: 폴 상호작용", "포스트: Before-After"]
    ideas = []
    for pillar in [pillar1, pillar2, pillar3]:
        print(f"\n[마인드맵: {pillar} (20 아이디어, 조회수 50만+ 포텐셜: viral hooks like vulnerability)]")
        for i in range(20):
            fmt = random.choice(formats)
            idea = f"Idea {i+1}: {fmt} - {pillar} 관련 '{random.choice(['Before-After', 'Quick Tip', 'Challenge', 'Story Share'])}' (e.g., Hootsuite BGM 추가)."
            ideas.append(idea)
            print(idea)
    
    # 캘린더: 초창기(기본), 중간(repurposing), 수익화(CTA 추가)
    print("\n[주간 콘텐츠 캘린더 플랜]")
    print("월: Pillar1 릴스 (초창기: 기본 팁)")
    print("화: Pillar2 스토리 (중간: 여정 repurposing)")
    print("수: Pillar3 챌린지 (수익화: 제품 링크 CTA, MeetEdgar 스타일)")

if __name__ == "__main__":
    content_planning()
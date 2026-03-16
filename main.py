import streamlit as st

st.set_page_config(
    page_title="MBTI 청소년 도서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 청소년 문학 추천 앱")
st.write("당신의 MBTI를 선택하면 어울리는 **청소년 문학 도서**를 추천해드립니다! ✨")

st.divider()

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

books = {

"INTJ":("📖 어린 왕자","깊은 생각과 철학적인 이야기를 좋아하는 INTJ에게 추천 ✨"),
"INTP":("📖 모모","시간과 삶의 의미를 생각하게 하는 이야기 ⏳"),
"ENTJ":("📖 해리포터","리더십과 도전이 가득한 판타지 세계 🧙"),
"ENTP":("📖 이상한 나라의 앨리스","기발한 상상력과 모험 가득한 이야기 🐇"),

"INFJ":("📖 연을 쫓는 아이","깊은 감정과 인간관계를 다루는 감동적인 이야기 💫"),
"INFP":("📖 나니아 연대기","순수한 상상력과 따뜻한 판타지 세계 ❄️"),
"ENFJ":("📖 Wonder","타인을 이해하는 마음을 배우는 감동 이야기 ❤️"),
"ENFP":("📖 빨간 머리 앤","밝고 상상력 넘치는 성장 이야기 🌸"),

"ISTJ":("📖 우리들의 일그러진 영웅","원칙과 정의를 생각하게 하는 이야기 ⚖️"),
"ISFJ":("📖 마당을 나온 암탉","따뜻하고 감동적인 성장 이야기 🐔"),
"ESTJ":("📖 로빈슨 크루소","생존과 책임을 다루는 모험 이야기 🏝️"),
"ESFJ":("📖 작은 아씨들","가족과 사랑을 다룬 따뜻한 이야기 👭"),

"ISTP":("📖 톰 소여의 모험","자유롭고 모험적인 이야기 🛶"),
"ISFP":("📖 별을 헤아리며","조용하지만 깊은 감동의 이야기 🌙"),
"ESTP":("📖 보물섬","짜릿한 모험과 탐험 이야기 🏴‍☠️"),
"ESFP":("📖 찰리와 초콜릿 공장","즐겁고 신나는 판타지 이야기 🍫")

}

if st.button("📖 책 추천 받기"):
    
    book, desc = books[mbti]

    st.balloons()

    st.success(f"✨ {mbti}에게 추천하는 책은!")

    st.subheader(book)
    st.write(desc)

    st.divider()
    st.write("💡 새로운 MBTI도 선택해보세요!")

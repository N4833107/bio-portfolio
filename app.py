import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="My Biology Portfolio",
    page_icon="🧬",
    layout="wide"
)

# --- Custom Background ---
def set_bg_from_url(image_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

set_bg_from_url("https://images.unsplash.com/photo-1581092580491-a206d58f2555?auto=format&fit=crop&w=1470&q=80")

# --- Custom Logo ---
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/DNA_icon.svg/1024px-DNA_icon.svg.png"
st.image(logo_url, width=100)
st.title("🔬 My Biology Portfolio")
st.markdown("#### Exploring Life Through Science")

# --- Content Sections ---
sections = {
    "My Passion for Biology": [
        "*\"Biology helps us uncover the secrets of life — and I am driven to be part of that discovery.\"*",
        "From the first time I engaged in a hands-on biology practical, I felt deeply inspired to understand how the human body works.",
        "Biology is not just a subject — it's a journey I want to explore as a future scientist."
    ],
    "Why I Want to Study Biology": [
        "A heart dissection in school sparked my curiosity about anatomy.",
        "A YouTube Short on genetic mutation fascinated me — how DNA changes impact whole organisms.",
        "Biology is essential to solving real-world medical and scientific problems."
    ],
    "School Lab Experiences": [
        "- **Heart Dissection Practical:** Identified atria, ventricles, and valves with precision.",
        "- **Food Tests & Respiration:** Measured glucose and oxygen to understand cellular energy.",
        "These taught me lab discipline, accuracy, and scientific thinking."
    ],
    "Self-Learning & Exploration": [
        "I watch educational videos and read articles on biology topics.",
        "- The process of sexual reproduction and its role in genetic diversity.",
        "- How oxygen and nutrients are delivered through the human transport system.",
        "Self-study deepened my passion and knowledge."
    ],
    "My Strengths & Future Goals": [
        "- **Strengths:** Focused, accurate in labs, strong memory, independent learner.",
        "- **Goal:** Become a biomedical/genetic researcher and improve healthcare.",
        "I'm ready to give my best — in labs, classrooms, and life."
    ]
}

# --- Display Sections ---
for title, points in sections.items():
    st.subheader(f"📌 {title}")
    for point in points:
        st.markdown(f"- {point}")
    st.markdown("---")

# --- Footer ---
st.markdown(f"""
<div style='text-align: center; font-size: 0.9em; color: gray;'>
Last updated: {datetime.today().strftime('%B %d, %Y')}
</div>
""", unsafe_allow_html=True)

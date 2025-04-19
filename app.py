import streamlit as st

st.set_page_config(page_title="Biology Portfolio", page_icon="🧬", layout="wide")

st.title("🧬 My Biology Portfolio")
st.markdown("Welcome to my biology journey! Scroll through to explore my interests, lab experiences, and future goals in the field of life sciences.")

# --- Section 1 ---
st.header("🌱 My Passion for Biology")
st.markdown("""
> *"Biology helps us uncover the secrets of life — and I am driven to be part of that discovery."*

From the first time I engaged in a hands-on biology practical, I felt deeply inspired to understand how the human body works. Since then, biology has become more than just a subject — it’s a field I want to explore and contribute to as a future scientist.
""")

# --- Section 2 ---
st.header("🧠 Why I Want to Study Biology")
st.markdown("""
- My interest in biology grew stronger after a heart dissection during school. Seeing the chambers, valves, and vessels in real life sparked my curiosity.
- A YouTube Short on **genetic mutation** amazed me — a single change in DNA can affect an entire organism!
- I explored topics like genetics, hereditary diseases, and reproductive biology.
""")

st.success("Biology is not just fascinating — it’s essential to improving lives.")

# --- Section 3 ---
st.header("🔬 School Lab Experiences")
st.markdown("""
- **Heart Dissection Practical:** I identified atria, ventricles, and valves, linking theory to real-life biology.
- **Food Tests & Respiration Experiments:** I ensured accuracy in measurements and understood how glucose and oxygen fuel our cells.

These experiences helped me develop **lab discipline**, **accuracy**, and **scientific thinking**.
""")

# --- Section 4 ---
st.header("📚 Self-Learning & Exploration")
st.markdown("""
Beyond school, I watch educational videos and explore topics like:

- **Sexual reproduction** and its role in genetic diversity
- **Human transport systems** — how oxygen and nutrients travel through our body
- **Gene therapy** and the future of medical innovation
""")

st.info("These topics fascinate me and fuel my goal to contribute to biomedical science.")

# --- Section 5 ---
st.header("🚀 My Strengths & Future Goals")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧩 Strengths")
    st.markdown("""
    - Highly focused during lab experiments  
    - Careful in following procedures  
    - Strong memory for biological concepts  
    - Independent learner
    """)

with col2:
    st.subheader("🎯 Goals")
    st.markdown("""
    - Become a scientist in **biomedical research** or **genetics**  
    - Contribute to healthcare discoveries  
    - Improve lives through science  
    """)

st.balloons()
st.markdown("💡 *This portfolio represents the first step in my scientific journey.*")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 - Biology Portfolio by Nabeel")

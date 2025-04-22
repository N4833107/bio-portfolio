import streamlit as st

st.set_page_config(page_title="Biology Portfolio", page_icon="🧬", layout="wide")

st.title("🧬 My Biology Portfolio")
st.markdown("""
Welcome to my digital biology journal! I’m **Nabeel**, an aspiring scientist driven by curiosity and compassion.  
From **lab practicals** to **creative projects**, every step I’ve taken is rooted in one dream:  
**To contribute meaningfully to the field of biotechnology and healthcare innovation.**

Scroll to discover my passion for life sciences, my journey through labs and self-learning,  
and the experiences that have shaped my dream to pursue **Biotechnology at Ngee Ann Polytechnic**.
""")

# --- Section 1 ---
st.header("🌱 My Passion for Biology")
st.markdown("""
> *"Biology is more than a subject — it's the key to understanding life, solving real-world problems, and making a difference through science."*  
> — *Nabeel, aspiring biotechnologist*

My fascination with biology began when I observed real organs during a heart dissection.  
Witnessing how the human body works — from the tiniest cell to entire organ systems — made me realize how much there is still to discover. That moment sparked my ambition to **explore the unknown**, and more importantly, to use science to **help others**.

Whether it's understanding **genetic conditions**, **molecular mechanisms**, or **biotech breakthroughs**, I find the mysteries of life endlessly captivating.
""")

# --- Section 2 ---
st.header("🧠 Why Biotechnology?")
st.markdown("""
- A YouTube Short on **CRISPR gene editing** showed me how biotechnology can literally rewrite the future of medicine.
- After a heart dissection, I stayed back to ask about **genetic heart conditions** — that moment connected classroom science to real-world impact.
- I regularly deep-dive into topics like **hereditary diseases**, **mutations**, and **genetic engineering** via books and educational content.
- I dream of being part of solutions — **curing genetic disorders** and enhancing lives using **biotechnological innovation**.

Biotechnology blends **biology, innovation, and compassion** — all values I hold deeply.  
It’s not just what I want to study — it’s the **lens through which I want to view the world**.
""")
st.success("I'm not just studying science. I'm preparing to use it to transform lives.")

# --- Section 3 ---
st.header("🔬 Lab Experiences That Inspired Me")
st.markdown("""
Practical work helped me discover my strengths in careful observation, precision, and discipline.

**Key experiments I loved:**
- 🫀 **Heart Dissection:** Identified atria, ventricles, and valves — where I truly connected theory to real anatomy.
- 🧪 **Food Tests:** Conducted Benedict’s, Biuret, and ethanol tests with accurate technique and confident analysis.
- 💨 **Respiration Practical:** Measured carbon dioxide using limewater and used respirometers — I appreciated how controls and small changes affect biological outcomes.

My approach:
- Always follow **lab safety** and hygiene
- Focus on **reliable, accurate results**
- Record and observe with **scientific discipline**
""")

# --- Section 4 ---
st.header("📚 Self-Driven Learning & Curiosity")
st.markdown("""
My learning never stops at school. I actively explore topics that fascinate me and link to biotechnology.

**Topics I’ve explored on my own:**
- 🔬 Genetic mutations and diseases like **cystic fibrosis**
- ❤️ Sexual reproduction & how it promotes **genetic diversity**
- 💉 Breakthroughs in **mRNA vaccines** and **stem cell therapy**
- 🩸 Capillaries and nutrient exchange in the circulatory system

I learn through:
- **CrashCourse**, **Khan Academy**, **Kurzgesagt**  
- Online science courses from **Cybrary**, **Cisco Networking**, and others  
- Research articles and YouTube explainers — I love breaking down complex topics and learning how they connect to real-life medicine  
""")
st.info("My initiative proves that I’m ready for independent learning in a polytechnic environment.")

# --- Section 5 ---
st.header("🚀 Strengths, Skills & Future Vision")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧩 Strengths")
    st.markdown("""
    - Detail-oriented in labs  
    - Strong memory for biological terms and systems  
    - Constantly ask “why” to understand deeply  
    - Great at connecting theory with real-world examples  
    - Explain biology clearly to others  
    - Motivated to learn independently
    """)

with col2:
    st.subheader("🎯 Future Goals")
    st.markdown("""
    - Enroll in **Biotechnology at Ngee Ann Polytechnic**  
    - Work on **genetic therapy research**  
    - Solve **real medical challenges** using biotechnology  
    - Contribute to **cutting-edge biomedical innovation**  
    - Educate and inspire others about the power of science
    """)

st.balloons()
st.markdown("💡 *This portfolio is more than a showcase — it's a glimpse into the future I’m working towards in life sciences.*")

# --- Section 6: DNT Project Related to Biology ---
st.header("💡 DNT Project: When Biology Meets Design Tech")

st.markdown("""
As part of my O-Level **Design & Technology coursework**, I created an **interactive infinity mirror lung display** to promote **organ donation awareness**, especially lung transplants.

🛠️ **What I Built:**
- A **red transparent acrylic lung** lit with LEDs  
- **Infinity mirror effect** symbolizing **endless hope** for transplant patients  
- Interactive visual design combining **biology, electronics, and public health**

📌 **What I Learned:**
- **Basic circuitry and LED integration**
- **CAD design** and hands-on acrylic fabrication
- Biological research on lung function and transplants
- Power of **design storytelling** in science communication

This experience proved how **creativity and science** can combine to **educate and inspire**, a skill I hope to bring into biotech.
""")

# --- Section 7: Why Ngee Ann Polytechnic? ---
st.header("🎓 Why Ngee Ann Polytechnic's Biotechnology Course?")
st.markdown("""
After reviewing NP’s **Diploma in Biotechnology**, I know this is the right environment for me.

**Modules I’m excited for:**
- 🧬 **Molecular Genetics & Bioinformatics**
- 🧫 **Cell Culture & Tissue Engineering**
- 🧪 **Applied Biochemistry**

What draws me most:
- Emphasis on **real-world labs** and **project-based learning**
- Opportunity to contribute to **innovative research**
- Pathways to solving real healthcare challenges

The **EAE route** allows me to show not just my grades, but my **drive, passion, and vision** for the future.
""")
st.success("I’m ready — not just to study biotechnology, but to contribute to its future.")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 - Biology Portfolio by Shaik Mohamed Nabeel | Built with ❤️ using Streamlit")


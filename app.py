import streamlit as st

st.set_page_config(page_title="Biology Portfolio", page_icon="🧬", layout="wide")

st.title("🧬 My Biology Portfolio")
st.markdown("""
Welcome to my biology journey! I'm Nabeel, a passionate aspiring scientist with a deep curiosity about life sciences and a clear goal: to contribute to the world of **biotechnology**. Scroll down to explore my interests, hands-on lab experiences, and personal reflections that have shaped my dream of pursuing Biotechnology at Ngee Ann Polytechnic.
""")

# --- Section 1 ---
st.header("🌱 My Passion for Biology")
st.markdown("""

> *"Biology is more than a subject — it's the key to understanding life, solving real-world problems, and making a difference through science."*  
> — *Nabeel, aspiring biotechnologist*


My fascination with biology began the moment I observed real organs during a heart dissection. Seeing how complex systems work together in the human body made me realize how much there is still to uncover — and that I wanted to be part of that discovery process. Whether it's understanding genetic conditions or exploring how cells function, I find the **mysteries of life** endlessly fascinating.
""")

# --- Section 2 ---
st.header("🧠 Why I Want to Study Biology — Especially Biotechnology")
st.markdown("""
- A YouTube Short about **CRISPR gene editing** opened my eyes to the future of medicine and biotechnology.
- After our heart dissection in school, I stayed back to ask my teacher about genetic heart conditions — that’s when I first heard about biotechnology applications in real-life medicine.
- I often explore topics like **hereditary diseases**, **mutations**, and **molecular biology** through books and videos.
- I want to be part of solving medical problems — like curing inherited diseases — using **biotechnology innovations**.

Biotechnology combines my love for biology and my problem-solving nature. I believe it’s the perfect path for me to **make a real-world impact**.
""")

st.success("I see myself not just studying science — but using it to change lives.")

# --- Section 3 ---
st.header("🔬 Real Lab Experiences that Shaped Me")
st.markdown("""
At school, I developed strong lab discipline and a love for precise, hands-on science.

- **Heart Dissection Practical:** I identified the atria, ventricles, valves, and vessels. This was my favorite moment in biology — the link between theory and real anatomy was inspiring.
- **Food Tests (Glucose, Starch, Protein, Fat):** I performed Benedict's and Biuret tests, learning to measure and interpret results accurately.
- **Respiration Experiments:** I used limewater and respirometers to investigate how the body uses oxygen. I learned the value of good controls and detailed observations.

I always ensured:
- **Clean and safe lab practices**
- **Consistent measurements**
- **Careful following of procedures**
""")

# --- Section 4 ---
st.header("📚 My Self-Learning in Biology & Beyond")
st.markdown("""
Outside of the classroom, I actively seek knowledge on topics that interest me, especially those that link to biotechnology.

**Topics I've explored independently:**
- Genetic mutations and how they lead to diseases like cystic fibrosis
- Sexual reproduction and how it promotes genetic diversity
- Human circulatory system and the role of capillaries in nutrient exchange
- Biotech breakthroughs like **stem cell therapy** and **mRNA vaccines**

I've also completed multiple online science courses and regularly watch **CrashCourse**, **Khan Academy**, and **Kurzgesagt** videos to deepen my understanding.
""")

st.info("This self-initiative shows my commitment to life sciences and readiness for a polytechnic environment.")

# --- Section 5 ---
st.header("🚀 Strengths, Skills & Future Goals")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🧩 Strengths")
    st.markdown("""
    - High attention to detail during lab work  
    - Strong memory — especially for scientific facts and concepts  
    - Able to link theory to real-life applications  
    - Curious and motivated to learn independently  
    - Always ask deeper 'why' questions  
    - Good at explaining biology concepts to others
    """)

with col2:
    st.subheader("🎯 Future Goals")
    st.markdown("""
    - Study **Biotechnology** at Ngee Ann Polytechnic  
    - Contribute to **genetic therapy research**  
    - Help solve medical challenges through **biomedical innovation**  
    - Eventually work in labs tackling real-world health issues  
    """)

st.balloons()
st.markdown("💡 *This portfolio is not just a summary — it’s a promise of what I hope to achieve in the field of biotechnology.*")

# --- Section: DNT Project Related to Biology ---
st.header("💡 DNT Project: Biology Meets Design Technology")

st.markdown("""
As part of my O-Level Design & Technology coursework this year, I created an **interactive infinity mirror lung display** to promote awareness about **organ donation**, specifically **lung transplants**.

🛠️ **What I built:**
- A glowing acrylic lung structure using red transparent acrylic and LED lighting  
- An **infinity mirror** effect that symbolizes **endless hope for patients** awaiting organ transplants  
- A pair of lungs made of infinity mirror with led strip inside it, representing technological innovation in healthcare

🔗 **Why it matters:**
This project allowed me to merge design, electronics, and **human biology**, turning medical awareness into an eye-catching, interactive display. It also reflects my passion for biology and public health communication.

📌 **Skills involved:**
- Basic electronics & circuit design  
- CAD design and precision fabrication  
- Biological research on lungs and organ donation  
- Creative storytelling through visual design

This experience showed me how **science, tech, and creativity** can come together to **educate and inspire others** — a skill I believe is valuable in the field of biotechnology.
""")

# --- EAE Relevance ---
st.header("🎓 Why Ngee Ann Polytechnic’s Biotechnology Course is Right for Me")
st.markdown("""
After studying the modules offered in NP's **Diploma in Biotechnology**, I’m especially excited about:

- **Molecular Genetics and Bioinformatics**  
- **Cell Culture and Tissue Engineering**  
- **Applied Biochemistry**

These topics align perfectly with my interests. I’m particularly drawn to how NP emphasizes **real-world research, lab experience, and innovation** — skills I know I’ll thrive in based on my current experiences.

The EAE path gives me the chance to **show who I really am** — not just through grades, but through my deep interest in biology and commitment to making a difference in healthcare.
""")

st.success("I believe I’m an excellent fit for this course — motivated, passionate, and ready to contribute.")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 - Biology Portfolio by Shaik Mohamed Nabeel | Built with ❤️ using Streamlit")

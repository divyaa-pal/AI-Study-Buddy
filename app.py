import streamlit as st

import PyPDF2

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI-Powered Study Buddy")
st.write("Smart AI assistant for students")



# ----------------------------
# PDF Upload
# ----------------------------
uploaded_file = st.file_uploader("📄 Upload PDF Notes", type="pdf")

pdf_text = ""

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    st.success("✅ PDF uploaded successfully!")

# ----------------------------
# Text Area
# ----------------------------
notes = st.text_area(
    "📝 Paste your study notes",
    value=pdf_text,
    height=250
)

# ----------------------------
# Generate Summary
# ----------------------------
if st.button("Generate Summary"):

    if notes.strip() == "":
        st.warning("Please enter notes!")
    else:
        sentences = notes.split(".")
        summary = ".".join(sentences[:3])

        st.subheader("📌 Summary")
        st.success(summary)

# ----------------------------
# Quiz Generator
# ----------------------------
if st.button("Generate Quiz"):

    if notes.strip() == "":
        st.warning("Please enter notes!")
    else:
        st.subheader("🧠 Quiz Questions")

        st.write("1. What is the main topic of the notes?")
        st.write("2. Explain the important concepts.")
        st.write("3. Write short notes on the topic.")
        st.write("4. What are the advantages discussed?")
        st.write("5. Summarize the chapter in your own words.")

# ----------------------------
# Flashcards
# ----------------------------
if st.button("Generate Flashcards"):

    if notes.strip() == "":
        st.warning("Please enter notes!")
    else:
        st.subheader("🃏 Flashcards")

        st.info("📌 Flashcard 1: Main Concept")
        st.info("📌 Flashcard 2: Important Definition")
        st.info("📌 Flashcard 3: Key Points")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.write("Developed by Divya Pal ❤️")
import streamlit as st
import PyPDF2
import google.generativeai as genai
st.set_page_config(page_title="AI Study Buddy", layout="centered")
# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------
# Page Config
# ----------------------------
st.markdown("""
<h1 style='text-align:center; color:blue;'>
📚 AI-Powered Study Buddy
</h1>
""", unsafe_allow_html=True)
st.write("Smart AI assistant for students")
# Gemini API Configuration
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")



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
        try:
            response = model.generate_content(
                f"Summarize these study notes:\n{notes}"
            )

            st.subheader("📌 Summary")
            st.success(response.text)

        except Exception:
            st.error("Gemini API quota reached. Please try again later.")

# ----------------------------
# Quiz Generator
# ----------------------------
if st.button("Generate Quiz"):

    if notes.strip() == "":
        st.warning("Please enter notes!")
    else:
        try:
            response = model.generate_content(
                f"Generate 5 quiz questions from these notes:\n{notes}"
            )

            st.subheader("🧠 Quiz Questions")
            st.write(response.text)

        except Exception:
            st.error("Gemini API quota reached. Please try again later.")

# ----------------------------
# Flashcards
# ----------------------------
if st.button("Generate Flashcards"):

    if notes.strip() == "":
        st.warning("Please enter notes!")
    else:
        try:
            response = model.generate_content(
                f"Create flashcards from these notes:\n{notes}"
            )

            st.subheader("🃏 Flashcards")
            st.write(response.text)

        except Exception:
            st.error("Gemini API quota reached. Please try again later.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.write("Developed by Divya Pal ❤️")
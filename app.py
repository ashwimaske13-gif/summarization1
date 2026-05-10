import streamlit as st

from utils import extract_text_from_pdf, split_text
from summarizer import generate_summary

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI-Based Text Summarization")
st.write("Upload PDF or enter text to generate summary.")

# Text Input
text_input = st.text_area(
    "Enter Text",
    height=250
)

# File Upload
uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# Summarize Button
if st.button("Generate Summary"):

    raw_text = ""

    # Case 1: Manual Text
    if text_input:
        raw_text = text_input

    # Case 2: PDF Upload
    elif uploaded_file:
        raw_text = extract_text_from_pdf(uploaded_file)

    else:
        st.warning("Please enter text or upload PDF.")
        st.stop()

    # Split long text
    chunks = split_text(raw_text)

    final_summary = ""

    with st.spinner("Generating summary..."):

        for chunk in chunks:
            summary = generate_summary(chunk)
            final_summary += summary + "\n"

    st.subheader("📌 Summary")
    st.success(final_summary)
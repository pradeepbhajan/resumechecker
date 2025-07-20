import streamlit as st
from checker import analyze_resume

st.set_page_config(page_title="Resume Checker", layout="centered")

st.title("📄 Resume Checker")
st.write("Upload your resume in **PDF** or **DOCX** format to get feedback.")

uploaded_file = st.file_uploader("Choose your resume file", type=["pdf", "docx"])

if uploaded_file is not None:
    with st.spinner("Analyzing your resume..."):
        data = uploaded_file.read()
        result = analyze_resume(data, uploaded_file.name)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(result["summary"])
            st.metric("Score", f"{result['score']} / 100")
            st.subheader("Suggestions:")
            for suggestion in result["suggestions"]:
                st.write("•", suggestion)

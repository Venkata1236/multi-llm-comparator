import streamlit as st
from llms.openai_model import get_openai_response
from llms.gemini_model import get_gemini_response
from llms.groq_model import get_groq_response
from utils.metrics import measure_time

st.set_page_config(page_title="Multi LLM Comparator", layout="wide")
st.title("Multi LLM Comparison Tool")

# -------------------------------
# User Input
# -------------------------------
query = st.text_area("Enter your query")

# -------------------------------
# Generate Button
# -------------------------------
if st.button("Generate"):

    if not query.strip():
        st.warning("Please enter a query.")
    else:
        col1, col2, col3 = st.columns(3)

        # -------------------------------
        # OpenAI Column
        # -------------------------------
        with col1:
            st.subheader("OpenAI (Cloud)")
            try:
                response, t = measure_time(get_openai_response, query)
                st.write(response)
                st.caption(f"Response Time: {t} seconds")
            except Exception as e:
                st.error(f"OpenAI Error: {e}")

        # -------------------------------
        # Gemini Column
        # -------------------------------
        with col2:
            st.subheader("Gemini (Google)")
            try:
                response, t = measure_time(get_gemini_response, query)
                st.write(response)
                st.caption(f"Response Time: {t} seconds")
            except Exception as e:
                st.error(f"Gemini Error: {e}")

        # -------------------------------
        # Groq Column
        # -------------------------------
        with col3:
            st.subheader("Groq (LLaMA 3.1)")
            try:
                response, t = measure_time(get_groq_response, query)
                st.write(response)
                st.caption(f"Response Time: {t} seconds")
            except Exception as e:
                st.error(f"Groq Error: {e}")
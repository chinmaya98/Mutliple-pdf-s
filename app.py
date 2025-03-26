import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
#from htmlTemplates import css, bot_template, user_template


def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    st.set_page_config(page_title="Chat with multiple PDFs",
                        page_icon=":books:")
    #st.write(css, unsafe_allow_html=True)
    st.title(":books: Chat with multiple PDFs")
    st.markdown("*Upload multiple pdf for quering*")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
        st.write(pdf_docs)
        

if __name__ == "__main__":
    main()
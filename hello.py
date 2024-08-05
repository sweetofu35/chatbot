import streamlit as st
from openai import OpenAI

st.title("코디 추천 앱 데모")

openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = openai_api_key

    if st.session_state.openai_api_key:
        st.session_state
        st.write("hello")
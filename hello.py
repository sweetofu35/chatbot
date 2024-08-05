import streamlit as st
from openai import OpenAI

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

if not st.session_state.logged_in:
    st.title("코디 추천 앱 demo")

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        st.session_state.openai_api_key = openai_api_key
        st.session_state.logged_in = True
        st.rerun()

if st.session_state.logged_in:
    st.title("환영합니다")
    for key, value in st.session_state.items():
        if key == "openai_api_key": openai_api_key = value

    client = OpenAI(api_key=openai_api_key)
    st.session_state


import streamlit as st
from openai import OpenAI

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("코디 추천 앱 demo")

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        st.session_state.logged_in = True

if not st.session_state.logged_in:
    st.title("환영합니다")

    client = OpenAI(api_key=openai_api_key)

    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = openai_api_key

    if st.session_state.openai_api_key:
        st.title("환영합니다")
        st.write("hello")
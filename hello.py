import streamlit as st
from openai import OpenAI

user_account = {"user":"1234", "user2":"0000"} #계정 정보
user_is_first = {"user":False, "user2":True} #고객의 첫 방문 여부
user_info = {"user":[95,28,255,"여성","동양인"]} #[상의 사이즈, 허리 사이즈, 신발 사이즈, 성별, 인종]
user_info_optional = {"user":[["상의","니트","ivory"],["하의","청바지","denim_blue"],["신발","운동화","black"]]} #[[옷 구분1, 옷 종류1, 색상1], [옷 구분2, 옷 종류2, 색상2], ...]

def login(username, password):
    if username in user_account and user_account[username] == password:
        return True
    else:
        return False

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

if not st.session_state.logged_in:
    st.title("코디 추천 앱 demo")

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    login_button = st.button("로그인")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        if login_button:
            if login(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state.openai_api_key = openai_api_key
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 잘못되었습니다.")

if st.session_state.logged_in:
    st.title("사전 세팅")
    openai_api_key =""
    for key, value in st.session_state.items():
        if key == "openai_api_key": openai_api_key = value

    client = OpenAI(api_key=openai_api_key)
    st.session_state


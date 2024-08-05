import streamlit as st
from openai import OpenAI

user_account = {"user":"1234", "user2":"0000"} #계정 정보
user_is_first = {"user":False, "user2":True} #고객의 첫 방문 여부
user_info = {"user":["여성","동양인",95,28,255]} #[성별, 인종, 상의 사이즈, 허리 사이즈, 신발 사이즈]
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

if 'username' not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in: # 로그인 화면
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

if st.session_state.logged_in: # 로그인 시 다음 페이지로 이동
    is_first = True
    openai_api_key =""
    for key, value in st.session_state.items():
        if key == "openai_api_key": openai_api_key = value

    client = OpenAI(api_key=openai_api_key)
    for key, value in user_is_first.items():
        if  key == st.session_state['username']: is_first = value
    if is_first: # 첫 방문 시 사전 정보 입력 페이지로 이동
        st.title("사전 정보 입력")
        if "page" not in st.session_state:
            st.session_state.page = 0
        if "gender" not in st.session_state:
            st.session_state.gender = ""
        if "race" not in st.session_state:
            st.session_state.race = ""
        if "top" not in st.session_state:
            st.session_state.top = 0
        if "bottom" not in st.session_state:
            st.session_state.bottom = 0
        if "foot" not in st.session_state:
            st.session_state.foot = 0
        if st.session_state.page == 0:
            st.session_state.gender = st.radio("성별을 선택해주세요",["**남성**", "**여성**"])
            st.session_state.race = st.radio("인종을 선택해주세요",["**동양인**", "**서양인**"])
            st.session_state.top = st.select_slider("상의 사이즈를 입력해주세요",options = [80,85,90,95,100,105,110,115,120,125,130])
            st.session_state.bottom = st.slider("하의 사이즈를 입력해주세요", 24, 35)
            st.session_state.foot = st.select_slider("발 사이즈를 입력해주세요", options = [230,235,240,245,250,255,260,265,270,275,280,285])

            if st.button("다음"):
                st.session_state.page = 1
                st.rerun()
        
        if st.session_state.page == 1:
            st.write(f"{st.session_state.username}님의 정보")
            st.write(f"성별 : {st.session_state.gender}")
            st.write(f"인종 : {st.session_state.race}")
            st.write(f"상의 사이즈 : {st.session_state.top}")
            st.write(f"하의 사이즈 : {st.session_state.bottom}")
            st.write(f"발 사이즈 : {st.session_state.foot}")
            st.write("입력한 내용이 확실합니까?")
            if st.button("예"):
                st.session_state.page = 2
                st.rerun()
            if st.button("아니오"):
                st.session_state.page = 0
                st.rerun()

        if st.session_state.page == 2:
            st.write("(선택) 가지고 있는 옷 정보를 입력하시겠습니까? (나중에 언제든지 다시 입력할 수 있습니다.)")
            if st.button("예"):
                st.session_state.page = 3
                st.rerun()
            if st.button("아니오"):
                for key, value in user_is_first:
                    if key == st.session_state.username: value = False
                #st.session_state.is_first = False
                st.session_state.page = 0
                st.rerun()

        if st.session_state.page == 3:
            st.write("옷 정보 입력하는 화면")

        
    else: # 재방문 시 메인 페이지로 이동
        st.title("메인 페이지")



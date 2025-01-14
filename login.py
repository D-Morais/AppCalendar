import streamlit as st
from utils import check_credentials


def verify_connect():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        st.title("Você não está conectado")
        return False

    st.sidebar.button("Sair", on_click=lambda: st.session_state.update({'logged_in': False}))
    return True


def user_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        with st.form(key="login_form"):
            st.subheader("Login")
            name = st.text_input("Nome do usuário")
            password = st.text_input("Senha", type="password")

            submit_button = st.form_submit_button("Entrar")

            if submit_button:
                if not name or not password:
                    st.error("Necessário preencher todos os campos.")
                    return
                if check_credentials(name, password):
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")
    else:
        st.title("Você está conectado")
        st.sidebar.button("Sair", on_click=lambda: st.session_state.update({'logged_in': False}))

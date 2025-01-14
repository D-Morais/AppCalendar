import streamlit as st
from script_db import add_user
from utils import encrypt, verifi_exists_name


def register_user():
    with st.form(key="register_form"):
        st.subheader("Novo Usuário")

        new_username = st.text_input("Nome de usuário")
        new_password = st.text_input("Senha", type="password")
        repeat_password = st.text_input("Confirmar senha", type="password")

        submit_button = st.form_submit_button(label="Registrar")

        if submit_button:
            if not new_username or not new_password or not repeat_password:
                st.error("Necessário preencher todos os campos.")

            elif new_password != repeat_password:
                st.error("Senha e confirmação necessitam ser iguais")

            else:
                exists_username = verifi_exists_name(new_username)
                if exists_username:
                    st.error("Usuário já cadastrado no sistema.")
                else:
                    hashed_new_password = encrypt(new_password)
                    add_user(new_username, hashed_new_password)
                    st.success("Usuário adicionado com sucesso.")

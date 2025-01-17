import time

import streamlit as st
import re
from script_db import add_user, get_users, remove_user
from utils import encrypt, verifi_exists_name


def verify_email(email):
    standard = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(standard, email)


def register_user():
    st.subheader("Acesso ao Sistema")
    option_selected = st.selectbox("Escolha a opção desejada:", ["Adicionar", "Remover"])

    if option_selected == "Adicionar":
        with st.form(key="register_form"):
            st.subheader("Novo Usuário")

            new_username = st.text_input("Nome de usuário")
            new_email = st.text_input("E-mail")
            new_password = st.text_input("Senha", type="password")
            repeat_password = st.text_input("Confirmar senha", type="password")

            submit_button = st.form_submit_button(label="Registrar")

            if submit_button:
                required_fields = [new_username, new_email, new_password, repeat_password]

                if not all(required_fields):
                    st.error("Necessário preencher todos os campos.")

                elif new_password != repeat_password:
                    st.error("Senha e confirmação necessitam ser iguais")

                elif not verify_email(new_email):
                    st.error("Formato de e-mail inválido. Insira um e-mail correto.")

                else:
                    exists_username = verifi_exists_name(new_username)
                    if exists_username:
                        st.error("Usuário já cadastrado no sistema.")

                    else:
                        hashed_new_password = encrypt(new_password)
                        add_user(new_username, hashed_new_password)
                        st.success("Usuário adicionado com sucesso.")

    elif option_selected == "Remover":
        st.subheader("Lista de Funcionários com Acesso ao Sistema")
        users = get_users()
        list_users_selected = []

        if len(users) > 1:
            for user in users[1:]:
                if st.checkbox(user[0]):
                    list_users_selected.append(user[0])

            if st.button("Excluir"):
                if list_users_selected:
                    for user_selected in list_users_selected:
                        remove_user(user_selected)
                    st.success("Usuário(s) removido(s) com sucesso.")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Nenhum usuário selecionado.")
        else:
            st.warning("Não há funcionários cadastrados.")

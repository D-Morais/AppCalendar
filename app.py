import streamlit as st
from streamlit_option_menu import option_menu
from register_user import register_user
from login import user_login, verify_connect
from download import generate_relatorie
from home import app_home
from vacation_calendar import vacation_calendar


def run_app():
    st.set_page_config(page_title="Gerenciador de Férias", page_icon="📆")
    hide_st_style = """
                       <style> MainMenu {visibility: hidden;}
                               footer {visibility: hidden;}
                               header {visibility: hidden;}
                       </style>
                   """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Login", "Página Inicial", "Calendário de Férias", "Baixar Informações", "Adicionar Acesso"],
            icons=["box-arrow-in-right", "house", "calendar", "download", "person-add"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Login":
        user_login()

    elif selected == "Página Inicial":
        if verify_connect():
            app_home()

    elif selected == "Calendário de Férias":
        if verify_connect():
            vacation_calendar()

    elif selected == "Baixar Informações":
        if verify_connect():
            generate_relatorie()
    elif selected == "Adicionar Acesso":
        if verify_connect():
            register_user()


if __name__ == "__main__":
    run_app()

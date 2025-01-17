import streamlit as st
from streamlit_option_menu import option_menu
from manege_users import register_user
from login import user_login, verify_connect
from download import generate_relatorie
from home import app_home
from vacation_calendar import vacation_calendar
from manage_employee import manage_employees
from manage_vacation import manage_vacations


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
            options=["Início", "Calendário de Férias", "Gerenciar Férias", "Gerenciar Funcionários", "Gerenciar Acesso",
                     "Baixar Informações", "Login"],
            icons=["house", "calendar2-event", "calendar2-check", "person-gear", "building-gear", "download",
                   "box-arrow-in-right"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Início":
        app_home()

    elif selected == "Calendário de Férias":
        if verify_connect():
            vacation_calendar()

    elif selected == "Gerenciar Férias":
        if verify_connect():
            manage_vacations()

    elif selected == "Gerenciar Funcionários":
        if verify_connect():
            manage_employees()

    elif selected == "Gerenciar Acesso":
        if verify_connect():
            register_user()

    elif selected == "Baixar Informações":
        if verify_connect():
            generate_relatorie()

    elif selected == "Login":
        user_login()


if __name__ == "__main__":
    run_app()

import streamlit as st
from datetime import date, timedelta
from script_db import add_vacation, load_ferias_from_db


def manage_vacations():
    st.subheader("Gerenciar Férias")
    option = st.selectbox("Selecione a opção relacionada a férias desejada", ["Adicionar", "Remover"])
    if option == "Adicionar":
        with st.form(key="vacation_form"):

            name = st.text_input("Nome do Funcionário:")
            col1, col2 = st.columns((2, 2))
            start_date = col1.date_input("Início das Férias", min_value=date.today())
            end_date = col2.date_input("Fim das Férias", min_value=start_date + timedelta(days=1))

            if st.form_submit_button("Adicionar Férias"):
                if not name:
                    st.error("Necessário preencher todos os campos")
                    return
                days_absent = (end_date - start_date).days + 1
                add_vacation(name, start_date, end_date)
                st.success(f"Férias de {name} adicionadas ao banco de dados. Ele ficará {days_absent} ausentes.")
    elif option == "Remover":
        list_vacation = load_ferias_from_db()
        st.write(list_vacation)

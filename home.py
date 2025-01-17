import streamlit as st
from datetime import date, timedelta
from script_db import fetch_data_by_date_range


def app_home():
    st.title("Gerenciamento de Férias")

    # Exibição da tabela de férias
    st.write("")
    st.subheader("Férias dos próximos 30 dias")
    end = date.today() + timedelta(days=30)
    df_vacation = fetch_data_by_date_range(date.today(), end)
    st.dataframe(df_vacation, width=800, hide_index=True)

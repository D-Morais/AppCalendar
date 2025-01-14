import streamlit as st
from streamlit_calendar import calendar
from script_db import load_ferias_from_db, fetch_data_by_date_range


def vacation_calendar():
    option = st.selectbox("Selecione o modo a ser apresentado as férias", ["Tabela", "Calendário"])
    st.title("Calendário de Férias")
    if option == "Tabela":
        df_vacation = load_ferias_from_db()
        st.dataframe(df_vacation, width=800, hide_index=True)
    elif option == "Calendário":
        df_events = fetch_data_by_date_range("01-01-2024", "31-12-2025")
        events_dict = {row[0]: row[1] for row in df_events}
        print(events_dict)
        selected_date = calendar(
            events={events_dict},  # Eventos no calendário (opcional)

        )

        if selected_date:
            st.write(f"Você selecionou: {selected_date.strftime('%d/%m/%Y')}")

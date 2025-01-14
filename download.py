import streamlit as st
from utils import generate_pdf, generate_excel


def generate_relatorie():
    st.title("Gerar PDF/EXCEL")
    option_download = st.selectbox("Selecione o método para download", ["PDF", "EXCEL"])
    if option_download == "PDF":
        if st.button("Gerar .pdf"):
            if generate_pdf():
                st.success("Relatório gerado com scesso.")
            else:
                st.warning("Não existe nenhuma férias cadastrada")
    elif option_download == "EXCEL":
        if st.button("Gerar .xlsx"):
            if generate_excel():
                st.success("Relatório gerado com sucesso.")
            else:
                st.warning("Não existe nenhuma férias cadastrada")

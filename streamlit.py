import streamlit as st
from analise import *

st.title("Como o consumo de álcool pode afetar diretamente o desempenho escolar de adolescentes")

descricao = st.container(border= True)
descricao.text("Esta aplicação foi desenvolvida para que pudesse facilitar a visualização dos dados implementados")

st.subheader("Visualização das médias das notas pela idade.")
grafico1 = media_notas_idade()

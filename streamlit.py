import streamlit as st
from analise import *

st.title("Como o consumo de álcool pode afetar diretamente o desempenho escolar de adolescentes")

descricao = st.container(border= True)
descricao.text("Esta aplicação foi desenvolvida para que pudesse facilitar a visualização dos dados implementados")

st.subheader("Visualização das médias das notas pela idade.")
fig,df = media_notas_idade()
st.pyplot(fig)
st.dataframe(df)

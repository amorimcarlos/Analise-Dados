import streamlit as st
from analise import *

st.title("Como o consumo de álcool pode afetar diretamente o desempenho escolar de adolescentes")

descricao = st.container(border= True)
descricao.text("Esta aplicação foi desenvolvida para que pudesse facilitar a visualização dos dados implementados")

st.subheader("Visualização da média das notas pela idade.")
fig, medianotas = media_notas_idade()
st.pyplot(fig)
st.dataframe(medianotas)
st.markdown("Este gráfico mostra a média da nota G3 pela idade." "Pode-se perceber que ao envelhecer, as notas tendem a diminuir.")


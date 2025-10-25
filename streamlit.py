import streamlit as st
from analise import *

st.title("Como o consumo de álcool pode afetar diretamente o desempenho escolar de adolescentes")

descricao = st.container(border= True)
descricao.text("Esta aplicação foi desenvolvida para que pudesse facilitar a visualização dos dados implementados e analisados.")

st.subheader("Visualização da média das notas pela idade.")
fig, medianotas = media_notas_idade()
st.pyplot(fig)
st.markdown("Este gráfico mostra a média da nota G3 pela idade." "Pode-se perceber que ao envelhecer, as notas tendem a diminuir, porém aos 20 anos os jovens aparentam estar mais dedicados.")

st.subheader("Visualização da média do consumo de álcool entre as idades ")

fig2, media_alcoolM = media_alcool_idade()
st.pyplot(fig2)
st.markdown("Este gráfico mostra a média do consumo de álcool entre as idades.")

st.subheader("Visualização da média das notas pelo consumo de álcool")

fig3, medianotasM = media_notas_alcool()
st.pyplot(fig3)
st.markdown("Este gráfico mostra a média do consumo de álcool entre as idades.")
import streamlit as st
import pandas as pd
import pyperclip
from streamlit_modal import Modal

st.set_page_config("Notas Funeraria")
st.header("Dados funeraria")

nome = st.text_input("Nome completo do falecido:")
apelido = st.text_input("Apelido do Falecido: Ex: Mais conhecido como..., Filho de... , esposo de...")

dt_nasc = st.date_input("Data de nascimento:")
dt_falec = st.date_input("Data do falecimento: ")

horario_falec = st.time_input("Horario do falecimento: ")
end_sepultamento = st.text_input("Endereço do sepultamento: ")
horario_sepult = st.time_input("Digite o horario do sepultamento:")
velorio = st.selectbox("Selecione o endereço do velório", ["Funeraria", "Residencia", "outro..."])
if velorio == "outro...":
    local_velorio = st.text_input("Digite o local do velório")

texto_nota = f"""
🕊️ Nota de Falecimento 🕊️

É com profundo pesar que comunicamos o falecimento de {nome}, carinhosamente conhecido como {apelido}.

✝️ Horário do Falecimento: {horario_falec}
📆 Data do Nascimento: {dt_nasc}
📆 Data do Falecimento: {dt_falec}
🏡 Velório: {velorio if velorio != 'outro...' else local_velorio}
⚰️ Sepultamento: {end_sepultamento}
⏰ Horário do Sepultamento: {horario_sepult}

Rogamos a Deus que conforte o coração de familiares e amigos neste momento de dor. 🖤🙏
"""

btn_confirmar = st.button("Confirmar")
if btn_confirmar:
    modal = Modal("Dados confirmados", key="PopUp")
    with modal.container():
        st.title(f"{texto_nota}")
        pyperclip.copy(texto_nota)
        st.success("Nota de falecimento copiada para a área de transferência!")

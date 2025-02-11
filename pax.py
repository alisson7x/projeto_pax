import streamlit as st
from streamlit_modal import Modal
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import toml
import os

# Caminho para o arquivo secrets.toml na pasta gitignore
secrets_path = os.path.join(".streamlit", "secrets.toml")

# Carregar variáveis do arquivo secrets.toml
secrets = toml.load(secrets_path)

# Inicializar o Firebase (se ainda não estiver inicializado)
if not firebase_admin._apps:
    cred = credentials.Certificate(secrets["firebase"])
    firebase_admin.initialize_app(cred)

# Acessar o banco de dados Firestore
db = firestore.client()

# Configuração da página
st.set_page_config(page_title="Funerária Pax Regional",
                   page_icon="img_pax.png",
                   layout="centered")
st.image("img_pax.png")
st.title("Insira os dados corretamente!")
st.warning("Todos os campos devem ser preenchidos!")

# Entrada de dados
nome = st.text_input("Nome completo do falecido:")
apelido = st.text_input("Apelido do Falecido: Ex: Mais conhecido como..., Filho de..., Esposo de...")

dt_nasc = st.date_input("Data de nascimento:")
dt_falec = st.date_input("Data do falecimento:")

horario_falec = st.time_input("Horário do falecimento:")
end_sepultamento = st.text_input("Endereço do sepultamento:")
horario_sepult = st.time_input("Digite o horário do sepultamento:")
velorio = st.selectbox("Selecione o endereço do velório", ["Funeraria", "Residencia", "outro..."])
if velorio == "outro...":
    local_velorio = st.text_input("Digite o local do velório")

# Geração da nota de falecimento
texto_nota = f"""
🕊️ Nota de Falecimento 🕊️

É com profundo pesar que comunicamos o falecimento de {nome}, carinhosamente conhecido como {apelido}.

✝️ Horário do Falecimento: {horario_falec.strftime('%H:%M')}
📆 Data do Nascimento: {dt_nasc.strftime('%d/%m/%Y')}
📆 Data do Falecimento: {dt_falec.strftime('%d/%m/%Y')}
🏡 Velório: {velorio if velorio != 'outro...' else local_velorio}
⚰️ Sepultamento: {end_sepultamento}
⏰ Horário do Sepultamento: {horario_sepult.strftime('%H:%M')}

Rogamos a Deus que conforte o coração de familiares e amigos neste momento de dor. 🖤🙏
"""

# Função para salvar dados no Firestore
def salvar_dados(nome, apelido, dt_nasc, dt_falec, horario_falec, end_sepultamento, horario_sepult, velorio, local_velorio=None):
    dados = {
        "nome": nome,
        "apelido": apelido,
        "data_nascimento": dt_nasc.strftime("%d/%m/%Y"),
        "data_falecimento": dt_falec.strftime("%d/%m/%Y"),
        "horario_falecimento": horario_falec.strftime("%H:%M"),
        "endereco_sepultamento": end_sepultamento,
        "horario_sepultamento": horario_sepult.strftime("%H:%M"),
        "local_velorio": velorio if velorio != "Outro" else local_velorio,
        "timestamp": datetime.now(),
    }

    db.collection("funeraria").add(dados)
    st.success("Dados salvos com sucesso!")

# Botão de confirmação
btn_confirmar = st.button("Confirmar")

if btn_confirmar:
    # Salvar os dados no Firestore
    salvar_dados(nome, apelido, dt_nasc, dt_falec, horario_falec, end_sepultamento, horario_sepult, velorio or local_velorio)
    
    # Exibe o modal com os dados confirmados
    modal = Modal("Dados confirmados!", key="PopUp")
    
    with modal.container():
        st.markdown(texto_nota)
        st.success("Dados enviados para a equipe PAX✅")

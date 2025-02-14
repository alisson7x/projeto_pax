import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import toml
import os

# Caminho para o arquivo secrets.toml na pasta gitignore
secrets_path = os.path.join("streamlit", "secrets.toml")

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
                   layout="wide"
                   )
st.image("img_pax.png", width=333)
st.title("Insira os dados corretamente!")
st.info("Todos os campos devem ser preenchidos!")

# Entrada de dados
nome = st.text_input("Nome completo do falecido:")
apelido = st.text_input("Apelido do falecido (Ex: Mais conhecido como..., Filho de..., esposo de...)")

# Entradas de data
dt_nasc_input = st.text_input("Data de nascimento (DD/MM/YYYY):")
dt_falec_input = st.text_input("Data do falecimento (DD/MM/YYYY):")

horario_falec = st.time_input("Horário do falecimento:")
end_sepultamento = st.text_input("Endereço do sepultamento:")
horario_sepult = st.time_input("Digite o horário do sepultamento:")
velorio = st.selectbox("Selecione o endereço do velório", ["Funeraria", "Residencia", "outro..."])
local_velorio = st.text_input("Digite o local do velório") if velorio == "outro..." else velorio

# Função para validar e converter datas
def validar_formatar_data(data_input):
    try:
        data_date = datetime.strptime(data_input, "%d/%m/%Y")
        return data_date, True
    except ValueError:
        return None, False

# Validação das datas
dt_nasc, dt_nasc_valida = validar_formatar_data(dt_nasc_input)
dt_falec, dt_falec_valida = validar_formatar_data(dt_falec_input)

# Validação adicional
if dt_nasc_valida and dt_falec_valida:
    if dt_falec < dt_nasc:
        st.error("A data de falecimento não pode ser anterior à data de nascimento.")
    elif dt_falec > datetime.now():
        st.error("A data de falecimento não pode ser no futuro.")
else:
    if not dt_nasc_valida:
        st.error("Data de nascimento inválida. Use o formato DD/MM/YYYY.")
    if not dt_falec_valida:
        st.error("Data de falecimento inválida. Use o formato DD/MM/YYYY.")

# Geração do texto
if dt_nasc_valida and dt_falec_valida and nome and apelido and end_sepultamento:
    texto_nota = f"""
    🕊️ Nota de Falecimento 🕊️

    É com profundo pesar que comunicamos o falecimento de {nome}, carinhosamente conhecido como {apelido}.\n

    ✝️ Horário do Falecimento: {horario_falec.strftime('%H:%M')}\n
    📆 Data de Nascimento: {dt_nasc.strftime('%d/%m/%Y')}\n
    📆 Data de Falecimento: {dt_falec.strftime('%d/%m/%Y')}\n
    🏡 Velório: {local_velorio}\n
    ⚰️ Sepultamento: {end_sepultamento}\n
    ⏰ Horário do Sepultamento: {horario_sepult.strftime('%H:%M')}\n

    Rogamos a Deus que conforte o coração de familiares e amigos neste momento de dor. 🖤🙏\n
    """

    # Exibição do texto da nota
    st.markdown("### Nota de Falecimento Gerada:")
    st.code(texto_nota, language="markdown")

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
        "local_velorio": velorio if velorio != "outro..." else local_velorio,
        "timestamp": datetime.now(),
    }

    db.collection("funeraria").add(dados)
    st.success("Dados salvos com sucesso!")

# Botão de confirmação
btn_confirmar = st.button("Confirmar")

if btn_confirmar:
    if dt_nasc_valida and dt_falec_valida and nome and apelido and end_sepultamento:
        salvar_dados(nome, apelido, dt_nasc, dt_falec, horario_falec, end_sepultamento, horario_sepult, velorio, local_velorio)
    else:
        st.error("Por favor, preencha todos os campos obrigatórios corretamente!")

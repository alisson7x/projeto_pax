import streamlit as st
from datetime import datetime
import clipboard

# Configuração da página
st.set_page_config(
    page_title="Funerária Pax Regional",
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

# Apenas gerar texto se todos os dados estiverem válidos
if (
    dt_nasc_valida and dt_falec_valida
    and nome and apelido and end_sepultamento
):
    texto_nota = f"""
    🕊️ Nota de Falecimento 🕊️

    É com profundo pesar que comunicamos o falecimento de {nome}, carinhosamente conhecido como {apelido}.\n

    ✝️ Horário do Falecimento: {horario_falec.strftime('%H:%M')}\n
    📆 Data de Nascimento: {dt_nasc.strftime('%d/%m/%Y')}\n
    📆 Data de Falecimento: {dt_falec.strftime('%d/%m/%Y')}\n
    🏡 Velório: {local_velorio}\n
    ⚰️ Sepultamento: {end_sepultamento}\n
    ⏰ Horário do Sepultamento: {horario_sepult.strftime('%H:%M')}\n

    Rogamos a Deus que conforte o coração de familiares e amigos neste momento de dor. 🖤🙏
    """
    
    # Exibição da nota
    if st.button("Confirmar"):
        st.markdown("### Nota de Falecimento Gerada:")
        st.divider()
        st.write(texto_nota)
        st.success("Nota gerada com sucesso!")
        
        # Botão para copiar o texto para a área de transferência
    if st.button("Copiar Nota"):
        clipboard.copy(texto_nota)
        st.success("Nota copiada para a área de transferência!")
           
else:
    st.warning("Preencha todos os campos obrigatórios e valide os dados antes de gerar a nota.")




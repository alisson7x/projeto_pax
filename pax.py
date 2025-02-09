import streamlit as st
from streamlit_modal import Modal

# Configuração da página
st.set_page_config(page_title="Notas Funerária", layout="centered")
st.header("Dados Funerária")

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

# Botão de confirmação
btn_confirmar = st.button("Confirmar")

if btn_confirmar:
    # Exibe o modal com os dados confirmados
    modal = Modal("Dados confirmados", key="PopUp")
    with modal.container():
        st.title("Nota de Falecimento")
        st.write(texto_nota)

        # Botão para copiar a nota de falecimento usando JavaScript
        st.markdown(
            f"""
            <textarea id="textoNota" style="display:none;">{texto_nota}</textarea>
            <button onclick="copiarTexto()">Copiar nota de falecimento</button>
            <script>
                function copiarTexto() {{
                    var texto = document.getElementById("textoNota");
                    texto.select();
                    document.execCommand('copy');
                    alert('Nota de falecimento copiada para a área de transferência!');
                }}
            </script>
            """,
            unsafe_allow_html=True
        )

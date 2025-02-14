# Funerária Pax Regional - Gerador de Nota de Falecimento

Este é um aplicativo desenvolvido com **Streamlit** para gerar notas de falecimento de forma rápida e organizada.

## 📌 Funcionalidades
- Interface amigável para preenchimento de dados.
- Validação de datas para evitar erros.
- Geração automática da nota de falecimento.
- Opção para copiar a nota gerada para a área de transferência.

## 🛠️ Tecnologias Utilizadas
- **Python** (linguagem principal)
- **Streamlit** (para criação da interface)
- **Pyperclip** (para funcionalidade de copiar texto)

## 🚀 Como Executar o Projeto
### 1️⃣ Clone este repositório:
```bash
 git clone https://github.com/seu-usuario/projeto-pax.git
 cd projeto-pax
```
### 2️⃣ Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Execute a aplicação:
```bash
streamlit run app.py
```

## 📋 Campos do Formulário
- **Nome completo**
- **Apelido**
- **Data de nascimento** (DD/MM/YYYY)
- **Data de falecimento** (DD/MM/YYYY)
- **Horário do falecimento**
- **Endereço do sepultamento**
- **Horário do sepultamento**
- **Local do velório** (selecionável)

## 🔍 Validações Implementadas
- Impede que a data de falecimento seja anterior à data de nascimento.
- Bloqueia datas de falecimento no futuro.
- Alerta caso os campos não estejam preenchidos corretamente.

## 📌 Observação
Se a funcionalidade de **copiar a nota** não funcionar em alguns ambientes, pode ser necessário copiar manualmente o texto gerado.

---
💡 *Desenvolvido para facilitar a elaboração de notas de falecimento com rapidez e precisão.*


#  Gerador de Notas de Falecimento

## ✨ Sobre o projeto

Este projeto foi desenvolvido para auxiliar funerárias a gerarem notas de falecimento de forma rápida e eficiente. A aplicação foi criada utilizando **Streamlit**, permitindo uma interface intuitiva e de fácil uso.

## 📚 Tecnologias Utilizadas

- **Python** – Linguagem principal do projeto.
- **Streamlit** – Framework para criação da interface web.
- **Datetime** – Biblioteca para manipulação de datas e horários.
- **Streamlit Modal** – Para exibição de pop-ups de confirmação.

## 🔧 Como Executar o Projeto

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/alisson7x/projeto_pax
   ```
2. **Acesse a pasta do projeto**:
   ```sh
   cd gerador-nota-falecimento
   ```
3. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   ```
4. **Instale as dependências**:
   ```sh
   pip install -r requirements.txt
   ```
5. **Execute a aplicação**:
   ```sh
   streamlit run app.py
   ```
6. **Acesse no navegador**:
   O Streamlit abrirá automaticamente uma página no navegador. Se não abrir, acesse manualmente: [http://localhost:8501](http://localhost:8501)

## 🔍 Funcionalidades

- Entrada de dados sobre o falecido (nome, apelido, datas, horários, endereço do sepultamento).
- Validação automática das datas.
- Geração de um texto padronizado para a nota de falecimento.
- Modal para exibição e cópia manual da nota gerada.

## 🛠 Melhorias Futuras

- Botão de cópia automática do texto gerado.
- Integração com um banco de dados para armazenar histórico de notas.
- Opção para exportar a nota em PDF.

## ✨ Contribuição

Sinta-se à vontade para contribuir com melhorias! Basta seguir os passos:

1. Fork o repositório.
2. Crie uma nova branch: `git checkout -b minha-feature`
3. Faça suas alterações e commite: `git commit -m "Adicionando nova funcionalidade"`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Abra um Pull Request.

## 👥 Autor

Criado por [www.linkedin.com/in/araujo-s](http://www.linkedin.com/in/araujo-s) – Entre em contato para feedbacks e colaborações!

---

🔗 **Repositório no GitHub**: [https://github.com/alisson7x/projeto\_pax](https://github.com/alisson7x/projeto_pax)

import streamlit as st
import requests

# 1. Configuração que remove margens bobas
st.set_page_config(page_title="Math Tech", page_icon="➕", layout="centered")

# 2. O "Pulo do Gato": CSS para esconder o que é feio e deixar visual de App
st.markdown("""
    <style>
    /* Esconde barra do GitHub, Menu e Rodapé */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Remove espaços vazios e define fundo preto real */
    .block-container {padding-top: 0rem; padding-bottom: 0rem;}
    .stApp {background-color: #000000;}
    
    /* Estilo dos Botões do Souza (Neon e Arredondado) */
    div.stButton > button {
        width: 100%; 
        border-radius: 15px; 
        height: 70px; 
        background-color: #111111; 
        color: #00FF99; 
        border: 2px solid #00FF99;
        font-weight: bold; 
        font-size: 16px;
        margin-bottom: -10px;
    }
    
    /* Estilo da Caixa de Texto */
    .stTextInput>div>div>input {
        background-color: #1a1a1a; 
        color: white; 
        border: 1px solid #00FF99;
        text-align: center;
    }
    
    /* Ajuste de cor dos textos e mensagens */
    .stMarkdown, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.markdown("<h1 style='text-align: center; color: white;'>➕ MATEMÁTICA<br><span style='color: #00FF99;'>TECH</span></h1>", unsafe_allow_html=True)

# Campo de entrada
pergunta = st.text_input("", placeholder="Digite sua dúvida aqui...")

# Função da IA
def chamar_ia(prompt_sistema, texto):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": "Bearer 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"}
    data = {
        "messages": [{"role": "system", "content": prompt_sistema}, {"role": "user", "content": texto}],
        "model": "llama-3.1-8b-instant"
    }
    try:
        r = requests.post(url, headers=headers, json=data)
        return r.json()['choices'][0]['message']['content']
    except:
        return "Erro de conexão ⚠️"

# 3. Organização em Colunas (Para não ficar "paia" no celular)
col1, col2 = st.columns(2)

with col1:
    if st.button("👨‍🏫\nPROFESSOR"):
        if pergunta:
            st.info(chamar_ia("Explique como um professor legal.", pergunta))

    if st.button("📸\nCÂMERA"):
        if pergunta:
            st.info(chamar_ia("Simule um scan de imagem técnica.", pergunta))

with col2:
    if st.button("📖\nDIRETO"):
        if pergunta:
            st.success(chamar_ia("Dê apenas a resposta direta.", pergunta))

    if st.button("♻️\nRESETAR"):
        st.rerun()

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("DESENVOLVIDO POR SOUZA")

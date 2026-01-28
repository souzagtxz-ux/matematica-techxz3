import streamlit as st
import requests

# Configuração da página (Estilo App de Celular)
st.set_page_config(page_title="Matemática Tech", page_icon="➕", layout="centered")

# CSS para deixar o visual preto e verde neon, idêntico ao seu projeto original
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #00FF99; text-align: center; font-family: sans-serif; }
    .stTextInput>div>div>input {
        background-color: #1a1a1a; color: white; border: 1px solid #00FF99; border-radius: 10px;
    }
    div.stButton > button {
        width: 100%; border-radius: 15px; height: 80px; 
        background-color: #1a1a1a; color: #00FF99; border: 2px solid #00FF99;
        font-weight: bold; font-size: 18px; transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #00FF99; color: black; }
    .stMarkdown { color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>➕ MATEMÁTICA TECH</h1>", unsafe_allow_html=True)

# Campo de entrada
pergunta = st.text_input("", placeholder="Digite sua dúvida matemática aqui...")

# Função de conexão com a IA Groq (Usando sua chave)
def perguntar_ia(prompt_sistema, texto_usuario):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": texto_usuario}
        ],
        "model": "llama-3.1-8b-instant"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    except:
        return "Erro de conexão ⚠️ Tente novamente."

# Layout de Botões (2 colunas como no seu Kivy)
col1, col2 = st.columns(2)

with col1:
    if st.button("👨‍🏫\nPROFESSOR"):
        if pergunta:
            with st.spinner('Analisando...'):
                res = perguntar_ia("Aja como um professor 👨‍🏫. Explique detalhadamente.", pergunta)
                st.info(res)
    
    if st.button("📸\nCÂMERA"):
        if pergunta:
            with st.spinner('Escaneando...'):
                res = perguntar_ia("Aja como um scanner de imagem técnico 📸.", pergunta)
                st.info(res)

with col2:
    if st.button("📖\nDIRETO"):
        if pergunta:
            with st.spinner('Calculando...'):
                res = perguntar_ia("Responda apenas o resultado final 📖.", pergunta)
                st.success(res)
            
    if st.button("♻️\nRESETAR"):
        st.rerun()

st.markdown("---")
st.caption("MATH TECH v1.0 | DESENVOLVIDO POR SOUZA")

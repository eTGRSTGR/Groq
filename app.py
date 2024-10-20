import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

# Carregar variáveis de ambiente do .env
load_dotenv()

# Verificar se a chave da API foi carregada
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Chave da API Groq não encontrada. Verifique o arquivo .env.")
    st.stop()

# Inicializar cliente Groq
client = Groq(api_key=api_key)

# Função para gerar resposta do chatbot
def chatbot_response(user_input, temperature=0.7):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",  # Modelo fixo
            temperature=temperature  # Ajuste da temperatura
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Ocorreu um erro ao processar sua solicitação: {e}"

# Customizar o layout
st.set_page_config(page_title="Chatbot com Groq API", page_icon="🤖", layout="wide")

# Barra lateral para informações adicionais
st.sidebar.title("Opções do Chatbot")
st.sidebar.write("Este chatbot usa a API Groq com o modelo LLaMA.")

# Slider para ajustar a temperatura
temperature = st.sidebar.slider("Temperatura", 0.0, 1.0, 0.7)

# Ajustar o título e descrição principal
st.title("

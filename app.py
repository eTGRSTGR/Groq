import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

# Carregar variáveis de ambiente do .env
load_dotenv()

# Inicializar cliente Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Função para gerar resposta do chatbot
def chatbot_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Customizar o layout
st.set_page_config(page_title="Chatbot com Groq API", page_icon="🤖", layout="wide")

# Barra lateral para informações adicionais
st.sidebar.title("Opções do Chatbot")
st.sidebar.write("Este chatbot usa a API Groq com o modelo LLaMA.")

# Ajustar o título e descrição principal
st.title("🤖 Chatbot Inteligente com Groq API")
st.write("**Faça uma pergunta para o chatbot abaixo!**")

# Caixa de entrada para o usuário
user_input = st.text_input("Digite sua pergunta aqui:", "")

# Estilo da caixa de resposta
st.markdown("<hr>", unsafe_allow_html=True)

# Exibir resposta quando o usuário enviar uma mensagem
if st.button("Enviar"):
    if user_input:
        response = chatbot_response(user_input)
        st.success(f"Chatbot: {response}")
    else:
        st.warning("Por favor, insira uma pergunta.")

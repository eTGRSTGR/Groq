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

# Configurar interface do Streamlit
st.title("Chatbot com Groq API")
st.write("Faça uma pergunta para o chatbot!")

# Caixa de entrada para o usuário
user_input = st.text_input("Você:", "")

# Exibir resposta quando o usuário enviar uma mensagem
if st.button("Enviar"):
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Chatbot: {response}")
    else:
        st.write("Por favor, insira uma pergunta.")


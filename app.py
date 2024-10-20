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
def chatbot_response(user_input, model="llama3-8b-8192", temperature=0.7):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=model,
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

# Seleção de modelo na barra lateral
model = st.sidebar.selectbox("Escolha o modelo", ["llama3-8b-8192", "llama2-13b", "gpt-4"])

# Slider para ajustar a temperatura
temperature = st.sidebar.slider("Temperatura", 0.0, 1.0, 0.7)

# Ajustar o título e descrição principal
st.title("🤖 Chatbot Inteligente com Groq API")
st.write("**Faça uma pergunta para o chatbot abaixo!**")

# Verificar se o estado da caixa de texto foi inicializado
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

# Caixa de entrada para o usuário
user_input = st.text_input("Digite sua pergunta aqui:", st.session_state['user_input'])

# Estilo da caixa de resposta
st.markdown("<hr>", unsafe_allow_html=True)

# Exibir resposta quando o usuário enviar uma mensagem
if st.button("Enviar"):
    if user_input:
        # Gerar a resposta usando o modelo e temperatura selecionados
        response = chatbot_response(user_input, model=model, temperature=temperature)
        st.success(f"Chatbot: {response}")
        
        # Limpar o valor da caixa de entrada após enviar a mensagem
        st.session_state['user_input'] = ''
        st.experimental_rerun()  # Atualiza a página para limpar o campo
    else:
        st.warning("Por favor, insira uma pergunta.")

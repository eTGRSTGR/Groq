import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Chave de API não encontrada. Verifique o arquivo .env")

print("Chave de API carregada corretamente.")

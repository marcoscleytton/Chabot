import argparse
from core.chatbot_basic import Chatbot
from core.qa_local import BancoDeDadosQA, Pergunta, Resposta
from core.chatbot_ai import ChatbotAI
import os

def run_basic():
    bot = Chatbot()
    while True:
        msg = input("Você: ")
        if msg.lower() == "fim": break
        print("Bot:", bot.get_response(msg))

def run_ai():
    bot = ChatbotAI(api_key=os.getenv("GOOGLE_API_KEY"))
    while True:
        msg = input("Você: ")
        if msg.lower() == "fim": break
        print("Bot:", bot.get_response(msg))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["basic","ai"], default="basic")
    args = parser.parse_args()

    if args.mode == "basic": run_basic()
    elif args.mode == "ai": run_ai()
class Chatbot:
    def __init__(self):
        self.responses = {
            "Olá": "Olá! Como posso ajudar você hoje?",
            "Qual é o seu nome?": "Eu sou um chatbot simples.",
            "Como você está?": "Estou apenas um código, mas obrigado por perguntar!",
        }

    def get_response(self, user_input):
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "Desculpe, não entendi sua pergunta."

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "fim":
            break
        print("Chatbot:", chatbot.get_response(user_input))
import google.generativeai as genai

class ChatbotAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_input):
        response = self.chat.send_message(user_input)
        return response.text
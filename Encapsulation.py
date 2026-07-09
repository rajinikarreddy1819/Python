class AIAssistant:
    def __init__(self):
        self.__api_key = "SK-123456"
        self.__model = "GPT-5"
        self.__temperature = 0.6
    def ask_questions(self, Query):
        print(f"Question: {Query}")
        self.__connect_to_model()
        print("Answer: Python inheritance allows one class to inherit another")
    def __connect_to_model(self):
        print(f"Connecting to {self.__model}......")
        print("Authenticating using API Key..........")
        print("Genetrating response......")
assistant = AIAssistant()
assistant.ask_questions("What is Inheritance ?")        

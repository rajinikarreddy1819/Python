class AIAssistant:
    def __init__(self, model_name):
        self.model_name = model_name
    def understand_prompt(self):
        print("Understanding the user's prompt....")
    def generate_res(self):
        print("Generating AI Response......")
    def safety_check(self):
        print("Checking response for safety......")
class CodingAssistant(AIAssistant):
    def write_code(self):
        print("Writing Python code ....")
    def debug_code(self):
        print("Finding bugs in the code .....")
class MedicalAssistant(AIAssistant):
    def explain_disease(self):
        print("Explaining disease information.......")
    def summarize_report(self):
        print("Sumarizing the medical report.....")

 # Creating Objects
coding_ai = CodingAssistant("GPT-5")
medical_ai = MedicalAssistant("GPT-5")

coding_ai.understand_prompt()
coding_ai.generate_res()
coding_ai.safety_check()

# Child-specific Methods
coding_ai.write_code()
coding_ai.debug_code()

print("-----------------------")

medical_ai.understand_prompt()
medical_ai.generate_res()
medical_ai.explain_disease()
medical_ai.summarize_report()

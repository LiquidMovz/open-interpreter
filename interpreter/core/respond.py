
import traceback
from codestral_client import CodestralClient

api_key = "Cya19eZaQFOwBpbVzfvAHXG5Cd8yffSn"
client = CodestralClient(api_key)

def generate_code(prompt):
    return client.get_completion(prompt)

def handle_chat(prompt):
    return client.chat(prompt)

class Respond:
    def attempt_LL_response(interpreter, user_prompt, messages):
        response = generate_code(user_prompt)
        messages.append(response)
        
    def proceed_with_LL(interpreter):
        user_message = handle_chat(process_message)

import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"
        
    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davince-003",
                prompt=user_input,
                max_tokens=4000,
                temperature=0.5
            ).choices[0].text
            return response
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I encountered an error and couldn't provide a response."

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hello, how are you?")
    print(response)

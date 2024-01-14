import openai

# Set your OpenAI GPT-3 API key
openai.api_key = "YOUR_API_KEY"


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine based on your needs
        prompt=prompt,
        max_tokens=150,  # You can adjust this based on the desired response length
    )
    return response.choices[0].text.strip()


# Start the conversation
print("Hello! I'm your GPT-3 ChatBot. Type 'quit' to exit.")
conversation_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("ChatBot: Goodbye!")
        break
    else:
        conversation_history.append(f"User: {user_input}")
        prompt = "\n".join(conversation_history)
        response = generate_response(prompt)
        conversation_history.append(f"ChatBot: {response}")
        print(f"ChatBot: {response}")

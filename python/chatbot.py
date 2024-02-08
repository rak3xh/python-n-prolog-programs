import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I am good, thank you!", "I am doing well."]),
    (r"what is your name", ["I am a chatbot. You can call me ChatBot."]),
    (r"quit", ["Goodbye!", "Bye for now."]),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm ChatBot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("ChatBot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

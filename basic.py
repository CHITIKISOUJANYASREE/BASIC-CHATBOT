# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    """Return chatbot responses based on user input."""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a simple Python chatbot 🤖."
    elif "how are you" in user_input:
        return "I'm doing great, thank you! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day 😊"
    else:
        return "I'm not sure I understand. Can you rephrase?"

def run_chatbot():
    """Main loop to run chatbot interaction."""
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()

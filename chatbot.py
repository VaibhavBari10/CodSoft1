# Define a dictionary with predefined responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I'm a simple chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
}

def chatbot_response(user_input):
    # Normalize the user input to lower case
    user_input = user_input.lower()
    
    # Iterate through the predefined responses
    for key in responses:
        if key in user_input:
            return responses[key]
    

    return "I'm sorry, I don't understand that."

def main():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
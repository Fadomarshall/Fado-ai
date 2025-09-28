print("Welcome to FADO AI!")

# Simple pre-defined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What’s up?",
    "how are you": "I’m just a program, but I’m doing great!",
    "bye": "Goodbye! Talk to you later.",
    "quit": "Goodbye! Talk to you later."
}

while True:
    user_input = input("You: ").lower() # convert input to lowercase

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        print("FADO AI: Bye!")
        break

    # Check if input matches a pre-defined response
    if user_input in responses:
        print("FADO AI:", responses[user_input])
    else:
        # Default fallback response
        print("FADO AI: I hear you -", user_input)
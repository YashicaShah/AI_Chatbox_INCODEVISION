print("Chatbot: Hello! I am a simple AI chatbot.")
print("Chatbot: Type 'bye' to exit.\n")
# Predefined questions and answers
responses = {
    # Greetings
    "hello": "Hi! How can I help you?",
    "hi": "Hello!",
    "hey": "Hey there!",
    "good morning": "Good morning! Have a great day.",
    "good evening": "Good evening! How can I help?",
    # Basic conversation
    "how are you": "I am doing well, thank you!",
    "what is your name": "I am a simple AI chatbot.",
    "your name": "I am a simple AI chatbot.",
    "who are you": "I am a chatbot created using Python.",
    "what can you do": "I can answer simple predefined questions.",
    "help": "You can ask me simple questions.",
    # Knowledge-based (simple)
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a popular programming language.",
    "what is chatbot": "A chatbot is a program that talks with users.",
    # Personal-style responses
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "sorry": "No problem!",
    # Exit
    "bye": "Goodbye! Have a nice day!",
    "exit": "Goodbye! See you soon!"
}
# Chatbot loop
while True:
    user_input = input("You: ").lower()
    # Exit condition
    if "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    matched = False
    # Basic text matching
    for key in responses:
        if key in user_input:
            print("Chatbot:", responses[key])
            matched = True
            break
    # If no match found
    if not matched:
        print("Chatbot: Sorry, I didn't understand that.")

import re

responses = {
    "greeting": [
        "Hello! 😊",
        "Hi there!",
        "Hey! How can I help you?"
    ],
    "education": [
        "I can help with college, exams, and projects.",
        "Are you asking about studies or exams?"
    ],
    "weather": [
        "I can’t check live weather, but it’s always a good idea to carry an umbrella 😄",
        "Weather depends on your location. Stay safe!"
    ],
    "help": [
        "I can chat about greetings, education, and weather.",
        "Try asking: 'Tell me about exams' or 'How is the weather?'"
    ],
    "exit": [
        "Goodbye! 👋",
        "See you soon!"
    ]
}

patterns = {
    "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",
    "education": r"\b(college|exam|study|project|subject)\b",
    "weather": r"\b(weather|rain|temperature|climate)\b",
    "help": r"\b(help|support|assist)\b",
    "exit": r"\b(bye|exit|quit|goodbye)\b"
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            return responses[intent][0], intent

    return "Sorry, I didn’t understand that. Can you rephrase?", None


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    reply, intent = chatbot_response(user_input)
    print("Chatbot:", reply)

    if intent == "exit":
        break

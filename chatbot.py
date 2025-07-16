print(" Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print("Bot: Hello! How can I help you?")
    elif "your name" in user_input:
        print("Bot: I'm Sakshi's friendly chatbot ")
    elif "how are you" in user_input:
        print("Bot: I'm doing great, thank you! How about you?")
    elif "weather" in user_input:
        print("Bot: I'm not a weather bot yet but it's always sunny with me!")
    elif "help" in user_input:
        print("Bot: I can tell you about me, the weather, or just chat!")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
    

    while True:  
        continue_chat = input("Do you want to continue chatting? (yes/no): ").lower()
        if continue_chat in ["yes", "no"]:
            break
        else:
            print("Please answer with 'yes' or 'no'.")    

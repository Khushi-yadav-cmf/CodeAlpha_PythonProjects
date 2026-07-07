def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to end the chat.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("🤖 ChatBot: Hi!")

        elif user == "how are you":
            print("🤖 ChatBot: I'm fine, thanks!")

        elif user == "what is your name":
            print("🤖 ChatBot: My name is SimpleBot.")

        elif user == "bye":
            print("🤖 ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")


chatbot()
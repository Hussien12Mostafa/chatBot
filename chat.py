import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("chatbot.aiml")

# Chat loop
print("AIMLBot: Hi there! How can I assist you? Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ").upper()
    if user_input == 'EXIT':
        print("AIMLBot: Goodbye!")
        break

    # Get a response from the chatbot
    response = kernel.respond(user_input)
    print("AIMLBot:", response)

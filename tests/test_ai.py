from ai.chat import ask_ai

print("JARVIS AI Test")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = ask_ai(user)

    print(f"\nJarvis: {reply}\n")
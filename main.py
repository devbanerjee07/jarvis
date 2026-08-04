from brain.brain import think

print("=" * 40)
print("         JARVIS")
print("=" * 40)

while True:

    command = input("You: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    think(command)
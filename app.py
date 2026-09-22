from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"))
client = OpenAI()

print("🤖 AI Agent is ready!")
print("Type 'exit' to stop.\n")

while True:

    # Take input from user
    user_message = input("You: ")

    # Stop the agent
    if user_message.lower() == "exit":
        print("Agent: Goodbye!")
        break

    # Send the message to the LLM
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="You are a helpful AI assistant for college students.",
        input=user_message
    )

    # Display the LLM's answer
    print("Agent:", response.output_text)

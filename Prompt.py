import openai

# Load your API key from environment variables
api_key = "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"

# Initialize the OpenAI client
openai.api_key = api_key

# Create a function to interact with the ChatGPT API
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Adjust as needed
    )
    return response.choices[0].text

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_bot(user_input)
    print("Bot:", response)

# Create a function to interact with the ChatGPT API
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Adjust as needed
    )
    return response.choices[0].text

# Create a function to get the prompt
def getPrompt(param):
    prompt = f"explain {param} to me in a concise and easy-to-understand way"
    return prompt

# Main loop
while True:
    user_input = input("Enter a financial term: ")
    if user_input.lower() == "exit":
        break

    prompt = getPrompt(user_input)
    response = chat_with_bot(prompt)
    print(f"Bot: {response}")

#GET ANSWER

def getAnswers(question):
    prompt = f"answer the following question in a concise and easy-to-understand way, keeping the response within 100 words: {question}"
    return prompt



user_question = input("Ask a question: ")
prompt = getAnswers(user_question)
response = chat_with_bot(prompt)
print("Bot:", response)


import openai

# Function to interact with the LLM
def ask_llm(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the desired model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # System instructions
            {"role": "user", "content": question}  # User's question
        ]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    question = "What is the capital of France?"
    print(ask_llm(question))

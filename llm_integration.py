import openai
openai.api_key = "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"

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

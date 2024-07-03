import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# get user input
user_input = input('Prompt: ')

# send request and get response
response = openai.ChatCompletion.create(
    model = 'gpt-4o',
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': user_input}
    ],
    temperature = 0.5,
    max_tokens = 1024
)

print(response)
print()
print(response.choices[0].message.content)
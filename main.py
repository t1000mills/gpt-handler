import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# initialize conversation with a system message
messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

# infinite loop to capture back and forth exchange
while True:

    # get user input
    user_input = input('ME: ')

    # add the user message to the conversation history
    messages.append({'role': 'user', 'content': user_input})

    # send request and get response
    response = openai.ChatCompletion.create(
        model = 'gpt-4o',
        messages = messages,
        temperature = 0.5,
        max_tokens = 1024
    )

    gpt_response = response.choices[0].message.content
    print(f'GPT: {gpt_response}')

    # add gpt's message to the conversation history
    messages.append({'role': 'assistant', 'content': gpt_response})
import os
from openai import OpenAI
import click
import logging

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# instantiate a new OpenAI() client while checking
# that the OPENAI_API_KEY environment variable is set
def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logger.error("OPENAI_API_KEY environment variable not set.")
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    client = OpenAI(api_key=api_key)
    return client


class ChatBuilder:
    def __init__(self, model='gpt-3.5-turbo', temp=0.5, max_tokens=1024):
        self.model = model
        self.messages = []
        self.temp = temp
        self.max_tokens = max_tokens

    def reset(self):
        self.model = 'gpt-3.5-turbo'
        self.messages = []
        self.temp = 0.5
        self.max_tokens = 1024

    def set_model(self, model):
        self.model = model
        return self

    def add_system_message(self, content):
        self.messages.append({'role': 'system', 'content': content})
        return self

    def add_user_message(self, content):
        self.messages.append({'role': 'user', 'content': content})
        return self

    def set_temp(self, temp):
        self.temp = temp
        return self

    def set_max_tokens(self, max_tokens):
        self.max_tokens = max_tokens
        return self

    def build(self):
        if not self.model:
            raise ValueError("Model must be set")
        return {
            'model': self.model,
            'messages': self.messages,
            'temperature': self.temp,
            'max_tokens': self.max_tokens
        }


@click.command("gpt")
@click.version_option("0.0.1", prog_name="gpt")
@click.option('-p', '--python-code-reviewer', type=click.File(mode="r"), nargs=1, help='Use the python pode reviewer role.')
@click.option('-m', '--model', type=click.STRING, nargs=1, help='Which GPT model to use')
@click.option('-k', '--temp', type=click.FloatRange(0, 2), nargs=1, help='Sets the temperature of the GPT')
@click.option('-t', '--max-tokens', type=click.IntRange(0, 128000), nargs=1, help='Sets the maximum number of tokens to use')
def gpt(python_code_reviewer, model, temp, max_tokens):

    client = get_openai_client()
    builder = ChatBuilder(model, temp, max_tokens)

    # Python Code Reviewer
    if python_code_reviewer:

        builder.add_system_message('You are a code review assistant. Provide detailed suggestions to improve the given Python code.')
        content = click.prompt('Describe the python code', type=click.STRING)
        # open file and read into memory
        with python_code_reviewer as file:
            content += file.read()
        builder.add_user_message(content)

        # send request and get response
        response = client.chat.completions.create(**builder.build())

        # print the response
        print(response.choices[0].message.content)

    # Helpful Assistant
    else:
        # initialize conversation with a system message
        builder.add_system_message('You are a helpful assistant.')

        # infinite loop to capture back and forth exchange
        while True:

            # get user input
            user_input = click.prompt('ME', type=click.STRING)

            builder.add_user_message(user_input)

            # send request and get response
            response = client.chat.completions.create(**builder.build())
            # pull the content out of the response object and print it
            gpt_response = response.choices[0].message.content
            print(f'\nGPT: {gpt_response}')

            # add gpt's message to the conversation history
            builder.add_system_message(gpt_response)





if __name__ == "__main__":
    gpt()
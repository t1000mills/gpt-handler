## GPT Chat Application

This Python application is an advanced CLI (Command Line Interface) utility for generating interactive dialogues using the OpenAI GPT models. It includes features such utilising specific GPT models, adjusting dialogue parameters such as temperature and token limits, and specialized functionalities like code review assistance using natural language processing.

### Features

- Choose GPT model versions dynamically.
- Adjust conversational parameters such as response "temperature" and maximum token count.
- Specialized mode for Python code review using natural language prompts.
- Continuous interactive dialogue capability in assistant mode.

### Prerequisites

Before you begin, ensure you have the following:
- Python 3.6+ installed on your machine.
- OpenAI API key - Set this in your environment variables as `OPENAI_API_KEY`.

### Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Usage

To start using the CLI tool, you can invoke it from the command line. Below are several examples of how you can use the tool:

**General Help and Versioning**

```bash
python gpt.py --help
python gpt.py --version
```

**Python Code Reviewer**

To use the application as a Python code reviewer:

```bash
python gpt.py --python-code-reviewer your_python_script.py
```

**Custom GPT Model and Parameters**

You can specify a model, temperature, and max tokens like so:

```bash
python gpt.py --model 'gpt-3.5-turbo' --temp 0.7 --max-tokens 1500
```

**Continuous Dialogue Session**

Start a continuous dialogue session with the assistant by simply running:

```bash
python gpt.py
```

### Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](#). You can also take a look at the [contributing guide](#).

### Support

If you have any feedback or need help, please reach out to us at support@example.com.

### License

Distributed under the MIT License. See `LICENSE` for more information.
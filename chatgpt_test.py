# Some tests with ChatGPT

import os
import openai
import configparser

# Load your API key from a config file
config = configparser.ConfigParser()
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, ".openai", "config.ini")
config.read(file_path)
openai.api_key =  config['DEFAULT']['OPENAI_API_KEY']

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

print(response.choices[0].text)


import openai
import langchain

from langchain.llms import OpenAI

davinci = OpenAI(model_name='text-davinci-003')

def main():
    
    api_path = "./secret.txt"
    openai.api_key=read_api_key(api_path)


def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

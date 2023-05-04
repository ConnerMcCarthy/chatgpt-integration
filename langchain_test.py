# Using langchain, tiktoken, and hugging face to train an openAI model

import openai
import os
import tiktoken



from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#tokenizer = tiktoken.get_encoding('cl100k_base')
tokenizer = tiktoken.get_encoding('p50k_base')

from datasets import load_dataset
data = load_dataset('ConnerMcCarthy/notes')

def main():

    api_path = "./secret.txt"
    api_key = read_api_key(api_path)
    llm = OpenAI(temperature=0.9, openai_api_key=api_key)
    davinci = OpenAI(model_name='text-davinci-003', openai_api_key=api_key)
    text = "Whats a good name for weather at the center of a galaxy?"
    #print(llm(text))
    #print(davinci(text))

    prompt = PromptTemplate(
        input_variables=["planet"],
        template="Make a rhyme all about the planet {planet}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    print(chain.run("Pluto")) #not a planet :(


def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )

if __name__ == '__main__':
    main()
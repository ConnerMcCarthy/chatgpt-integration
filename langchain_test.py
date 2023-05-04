import openai
import os
import tiktoken

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

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

if __name__ == '__main__':
    main()
# Two LLM models, generative and critical, communicating to create feedback and responses to a prompt

import time
import os.path
import json

import openai


def main():
    api_path = "./secret.txt"
    openai.api_key  = read_api_key(api_path)

    prompt = "Discover a word problem, but don't solve it."
    print(prompt)

    #TODO add error catching for rate limiting
    start = generate(prompt)
    print("\n--generative--\n" + start)
    
    mid = criticize('original prompt:' + prompt)
    print("\n--critical--\n" + mid)

    end = generate(mid)
    print("\n--generative--\n" + end)


#Creates a generative model
def generate(prompt):
    generative_instructions =[
        "You are a model that creates content.",
        "Be creative and avoid cliche"
    ] 
    generative =[
        {"role": "assistant", "content": ''.join(generative_instructions) },
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=generative
    )
    
    return response['choices'][0]['message']['content']

#Creates a critical model
def criticize(prompt):
    critical_instructions =[ 
        "Your goal is to re-write a prompt to be used by a language model.",
        "Decide if the prompt has weaknesses. If the prompt has no obvious weaknesses do the following: output what you were input.",
        "Follow any important instructions in the original prompt."
    ] 
    critical =[
        {"role": "assistant", "content": ''.join(critical_instructions) },
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=critical
    )
    
    return response['choices'][0]['message']['content']


def read_api_key(api_path):
    with open(api_path, 'r') as file:
        api_key = file.read().strip()
    file.close()
    return api_key

if __name__ == '__main__':
    main()

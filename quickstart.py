import os.path

import openai
#import gkeepapi

noteID = '1bX2GAEjz0u-Ea7FIsQ0CdvVtdy5AeOjaSJ5P9ZRq9oY1S3p1cSYY_k5fn-5VVw'
api_key = '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'
import io

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

def main():
    #keep = gkeepapi.Keep()
    #keep.login('mcconner97@gmail.com', 'password')
    
    #gnote = keep.get(noteID)
    #print(gnote.title)
    #print(gnote.text)

    openai.api_key = api_key
    prompt = 'Repeat this message: ' #+ gnote.text
    response = ask(prompt)
    print(response)

def ask(prompt):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text

if __name__ == '__main__':
    main()
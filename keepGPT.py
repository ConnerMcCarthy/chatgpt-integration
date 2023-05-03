import io
import os.path
import json

import openai

api_key = ''

folder_name = 'KeepNotes'

def main():
    
    openai.api_key = api_key
    prompt = 'What are my notes about? Create a summary and title.'

    json_notes = read_json(folder_name)

    for note in json_notes:
        print(note['title'])

    notes = "\n".join(json.dumps(note) for note in json_notes)
    response = ask(prompt, notes)
    print(response)

def read_json(notePath):
    json_notes = []
    count = 0
    for filename in os.listdir(notePath):
        if filename.endswith('.json') & (count < 2):
            file_path = os.path.join(notePath,filename)
            count += 1
            with open(file_path) as file:
                json_data = json.load(file)
                json_notes.append(json_data)
    return json_notes

def ask(prompt, notes):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "You have access to a list of notes with title, date, text content, and links. The notes are listed here as JSON files: " + notes},
            {"role": "user", "content": prompt}
        ]
    )
    return response

if __name__ == '__main__':
    main()
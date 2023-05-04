# Outline of chatGPT Gmail connection
# TODO gather emails from last day, summarize until there is a daily summary
# Written by ChatGPT to be edited later

import os
import openai
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Set up Gmail API credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Get a Gmail service object using the credentials."""
    creds = None
    if os.path.exists('token.json'):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_emails():
    """Get a list of emails from the Gmail inbox."""
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    email_list = []
    
    if messages:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_list.append(msg['snippet'])
    
    return email_list

def generate_response(email):
    """Generate a response from OpenAI's GPT-3.5 model based on the email text."""
    prompt = f"Email: {email}\nResponse:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Get emails from Gmail inbox
emails = get_emails()

# Process each email and generate a response using GPT-3.5
for email in emails:
    response = generate_response(email)
    print(f"Email: {email}")
    print(f"Response: {response}")
    print('-' * 50)
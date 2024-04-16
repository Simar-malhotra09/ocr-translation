import requests
import uuid
import json
import os

''' 
Uses microsoft azure translation services

'''
def translate_text(text, from_lang='ja', to_lang='en'):
    key =  "af3e88942e2549a69f98985b18a2a725"
 # Retrieving Azure key from environment variables
    if not key:
        raise ValueError("Azure key not found. Please set the 'azure_key' environment variable.")
    
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "eastus"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': from_lang,
        'to': [to_lang]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    translated_text = response[0]['translations'][0]['text']
    return translated_text

'''
# Example usage:
text_to_translate = '斜め駐車'  # Japanese text
translated_text = translate_text(text_to_translate)
print(translated_text)'''
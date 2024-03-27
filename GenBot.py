import requests
import streamlit as st

API_KEY = 'AIzaSyDPdhtBbGTQY2IqCy6ueD3MkXgIOscx-MY'
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

headers = {
    'Content-Type': 'application/json'
}

prompt = st.text_input("Type your question here")

data = {
    'contents': [
        {
            'parts': [
                {
                    'text': prompt
                }
            ]
        }
    ]
}

params = {
    'key': API_KEY
}

response = requests.post(API_URL, headers=headers, json=data, params=params)

if prompt:

    if response.status_code == 200:
        result = response.json()
        candidates = result.get('candidates', [])
        if candidates:
            first_candidate = candidates[0]
            content = first_candidate.get('content')
            if content:
                parts = content.get('parts', [])
                if parts:
                    generated_text = parts[0].get('text', '')
                    st.write(generated_text)
                else:
                    print('No parts found in the content.')
                    st.write('No parts found in the content.')
            else:
                print('No content found in the candidate.')
                st.write('No content found in the candidate.')
        else:
            print('No candidates found in the response.')
            st.write('No candidates found in the response.')
    else:
        print(f'Request failed with status code: {response.status_code}')
        print(response.text)

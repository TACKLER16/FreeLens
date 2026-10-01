import ollama

response = ollama.chat(
    model='moondream',
    messages=[
        {
            'role': 'user',
            'content': 'what do you see?',
            'images': ['D:\\loki.jpg']
        }
    ]
)

print(response['message']['content'])
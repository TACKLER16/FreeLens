import base64
import cv2
import requests
import ollama

def encode_frame(frame):
    ret, buffer = cv2.imencode('.jpg', frame)
    encoded = base64.b64encode(buffer).decode('utf-8')
    return encoded

def ask_gemini(frame, question, history):
    encoded = encode_frame(frame)
    new_message = {
    "role": "user",
    "parts": [
        {"text": question},
        {"inline_data": {"mime_type": "image/jpeg", "data": encoded}}
    ]
    }
    history.append(new_message)
    body = {"contents": history} 
    API_KEY = "YOUR_API_KEY_HERE"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=body, headers=headers)
        result = response.json()['candidates'][0]['content']['parts'][0]['text']
    except (KeyError, Exception) as e:
        print(f"Gemini failed: {e}, switching to moondream...")
        cv2.imwrite("temp.jpg", frame)
        moondream_response = ollama.chat(
            model='moondream',
            messages=[{
                'role': 'user',
                'content': question,
                'images': ['temp.jpg']
            }]
        )
        result = moondream_response['message']['content']
    history.append({
    "role": "model",
    "parts": [{"text": result}]
})
    return result, history
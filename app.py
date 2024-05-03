from flask import Flask, render_template, request, jsonify
import requests
import cv2 as cv
import pytesseract
import json
import os

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@app.route('/')
def reg():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part in the request", 400
    f = request.files['file']
    if f.filename == '':
        return "No selected file", 400
    
    file_path = os.path.join('uploads', f.filename)
    f.save(file_path)
    
    img = cv.imread(file_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    s = pytesseract.image_to_string(img)
    
    chatbot_url = "https://virtual-vaidhya.onrender.com/ask"
    response = requests.get(chatbot_url, params={"question": s})

    print (type(response))

    fetched_response = response.json()
    fetched_response_str = json.dumps(fetched_response)
    print(type(fetched_response_str))
    str_gain = fetched_response_str[13:]
    str_gain = str_gain[:-1]

    return render_template('result.html', response=str_gain)

if __name__ =='__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

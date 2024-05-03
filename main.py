from flask import Flask
import cv2 as cv
import pytesseract

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv.imread('img4.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

s = pytesseract.image_to_string(img)
print(pytesseract.image_to_string(img))

@app.route("/")

def main():
   return s

if __name__ =='__main__':
    #app.debug = True
    app.run(debug = True)
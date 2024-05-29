



import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
from ultralytics import YOLO
import time
from fun_camera1 import open
from keep_data import read_file_to_array



sentence=[]
read_file_to_array("sentence.txt",sentence)


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

choice = 0
moneFalse = 1
moneTrue =1
@app.route('/send', methods=['POST'])
def send():
    global choice
    global moneFalse
    global moneTrue
    data = request.get_json()
    if(data=='false'):
        choice += 1
    else:
        if (choice==1):
            moneTrue+=1
        else:
            moneFalse +=1
    message = open(sentence,choice,moneTrue,moneFalse)
    return jsonify(message), 200



if __name__ == '__main__':
    app.run(debug=True)







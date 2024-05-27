



import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
from ultralytics import YOLO
import time

from fun_camera1 import *



sentence =["my name is Sarah","20","Brown","Israel","Jerusalem"]


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
    print(data)
    if(data=='false'):
        choice += 1
    else:
        if (choice==1):
            moneTrue+=1
        else:
            moneFalse +=1
    print(moneFalse)
    message = open(sentence,choice,moneTrue,moneFalse)
    print(message)
    return jsonify(message), 200



if __name__ == '__main__':
    app.run(debug=True)


    """"
    
        def detect_objects_in_video(video_path):
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                print("Error: Could not open video file.")
                return

            model_path = "last.pt"
            print("Loading model...")
            start_time = time.time()
            model = YOLO(model_path)
            load_time = time.time() - start_time
            print(f"Model loaded in {load_time:.2f} seconds.")

            threshold = 0.2
            frame_count_with_objects = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("End of video.")
                    break

                results = model(frame)[0]

                for result in results.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = result

                    if score > threshold:
                        frame_count_with_objects += 1

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

            return frame_count_with_objects

        # קריאה לפונקציה והדפסת מספר הפריימים עם אובייקטים

        frame_count_with_objects = detect_objects_in_video("./uploads/video_received.mp4")
        print(f"Number of frames with objects: {frame_count_with_objects}")
        # חישוב תכונות
        audio="./uploads/audio_received.wav"
        features = extract_feature('audio', mfcc=True, chroma=True, mel=True)
        # חיזוי רגש
        predicted_emotion = model.predict(features)
        # פירוש התוצאה
        emotion_label1 = predicted_emotion[0]
        print(emotion_label1)

        response_data = {'message': 'Files uploaded successfully'}
        return jsonify(response_data)

    return jsonify({'error': 'Video and audio files are required'}), 400
    """




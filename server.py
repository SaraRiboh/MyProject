



import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
from ultralytics import YOLO
import time
from feelsModel import *
from From_mp4_to import *



sentence =["my name is Sarah","20","Brown","Israel","Jerusalem"]


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files and 'audio' in request.files:
        video_file = request.files['video']
        audio_file = request.files['audio']

        video_path = os.path.join(UPLOAD_FOLDER, "video_received.mp4")

        audio_path = os.path.join(UPLOAD_FOLDER, "audio_received.wav")

        video_file.save(video_path)
        audio_file.save(audio_path)

        # extract_audio_from_chrome_mp4("./uploads/video_received.mp4","output.wav")

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


if __name__ == '__main__':
    app.run(debug=True)




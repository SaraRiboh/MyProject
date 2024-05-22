"""
rom flask import Flask, request
from flask_cors import CORS
import os
import json
from flask import jsonify

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        video_file = request.files['video']
        video_path = os.path.join(UPLOAD_FOLDER, "D:/Downloads/video.mp4")
      #  video_path="D:/Downloads/video.mp4";
        video_file.save(video_path)

        # Do something with the video file here
        # For example, you can convert it to other formats
        # using ffmpeg or another library

        response_data = {'message': 'File uploaded successfully'}
        return jsonify(response_data)

    return jsonify({'error': 'Video file is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)

"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from From_mp4_to import *

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_path = os.path.join(UPLOAD_FOLDER, "video.mp4")
        audio_file.save(audio_path)

        input_file="video.mp4"
        output_file="output.wav"
        mp4_to_wav(input_file, output_file)



        # Do something with the audio file here
        # For example, you can process it or save it to a database

        response_data = {'message': 'File uploaded successfully'}
        return jsonify(response_data)

    return jsonify({'error': 'Audio file is required'}), 400


if __name__ == '__main__':
    app.run(debug=True)

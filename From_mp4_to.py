"""
from pydub import AudioSegment

def convert_wav(audio_def):
    song = AudioSegment.from_mp3(audio_def)
    wav_file = "final.wav"
    song.export(wav_file, format="wav")
    print(f"Converted {audio_def} to {wav_file}")
"""

# from moviepy.editor import VideoFileClip

import os
import shutil
import moviepy.editor

def extract_audio_from_chrome_mp4(mp4_file, audio_file):

    video = moviepy.editor.VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(audio_file)









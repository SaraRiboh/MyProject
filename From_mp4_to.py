from moviepy.editor import VideoFileClip


def mp4_to_wav(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)



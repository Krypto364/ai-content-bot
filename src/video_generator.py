# src/video_generator.py

from moviepy.editor import ImageClip, AudioFileClip
from gtts import gTTS

def create_video(text, image_path, output):

    # Generate voice
    tts = gTTS(text=text)
    audio_path = "assets/temp/audio.mp3"
    tts.save(audio_path)

    audio = AudioFileClip(audio_path)

    # Create simple video (image + audio)
    video = (
        ImageClip(image_path)
        .set_duration(audio.duration)
        .set_audio(audio)
        .resize((720, 1280))
    )

    video.write_videofile(output, fps=24)

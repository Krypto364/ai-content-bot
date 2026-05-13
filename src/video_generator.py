from moviepy.editor import *
from gtts import gTTS

def create_video(text, image_path, output):

    # Voice
    tts = gTTS(text=text)
    audio_path = "assets/temp/audio.mp3"
    tts.save(audio_path)

    audio = AudioFileClip(audio_path)

    # Background
    bg = ImageClip(image_path).set_duration(audio.duration).resize((720,1280))

    # Subtitles (split lines)
    lines = text.split(". ")

    clips = []
    duration_per_line = audio.duration / len(lines)

    for i, line in enumerate(lines):
        txt = TextClip(
            line,
            fontsize=45,
            color='white',
            method='caption',
            size=(680,200)
        ).set_position(("center", 900)).set_start(i * duration_per_line).set_duration(duration_per_line)

        clips.append(txt)

    video = CompositeVideoClip([bg, *clips]).set_audio(audio)

    video.write_videofile(output, fps=24)

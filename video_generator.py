from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
from gtts import gTTS

def create_video(text, image_path, output):
    # voice
    tts = gTTS(text=text)
    audio_path = "assets/temp/audio.mp3"
    tts.save(audio_path)

    audio = AudioFileClip(audio_path)

    bg = ImageClip(image_path).set_duration(audio.duration).resize((720,1280))

    txt = TextClip(
        text,
        fontsize=40,
        color='white',
        method='caption',
        size=(680,1000)
    ).set_position("center").set_duration(audio.duration)

    video = CompositeVideoClip([bg, txt]).set_audio(audio)

    video.write_videofile(output, fps=24)

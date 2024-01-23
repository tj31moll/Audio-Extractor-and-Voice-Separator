from moviepy.editor import VideoFileClip
from spleeter.separator import Separator

def extract_audio_from_video(video_path, audio_output_path):
    """
    Extracts the audio from a video file and saves it as an audio file.
    """
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output_path)
    print(f"Audio extracted to {audio_output_path}")

def separate_voices(audio_path, output_path):
    """
    Separates voices from the audio file using Spleeter.
    """
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, output_path)
    print(f"Voices separated in {output_path}")

# Example usage
video_path = 'path_to_your_video_file.mp4'  # Replace with your video file path
extracted_audio_path = 'extracted_audio.mp3'  # Replace with desired output audio file path
separate_output_path = 'path_for_separated_audio'  # Replace with desired output folder path

extract_audio_from_video(video_path, extracted_audio_path)
separate_voices(extracted_audio_path, separate_output_path)

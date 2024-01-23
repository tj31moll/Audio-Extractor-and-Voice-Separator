# Audio Extractor and Voice Separator

This script provides functionality to extract audio from video files and separate voices using `moviepy` and `spleeter`. It is a simple and efficient tool for audio processing tasks.

## Features

- **Extract Audio**: Extract audio tracks from video files.
- **Separate Voices**: Use `spleeter` to separate voices from the extracted audio.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3
- `moviepy` library
- `spleeter` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
   ```bash
   pip install moviepy spleeter
   ```

## Usage

1. Set the paths in the script:
   - `video_path`: Path to the video file.
   - `extracted_audio_path`: Path for the extracted audio file.
   - `separate_output_path`: Directory path for separated audio output.

2. Run the script:
   ```bash
   python script_name.py
   ```

### Functions

- `extract_audio_from_video(video_path, audio_output_path)`: Extracts audio from the given video file.
- `separate_voices(audio_path, output_path)`: Separates voices from the given audio file.

## Example

```python
video_path = 'path_to_your_video_file.mp4'  # Replace with your video file path
extracted_audio_path = 'extracted_audio.mp3'  # Replace with desired output audio file path
separate_output_path = 'path_for_separated_audio'  # Replace with desired output folder path

extract_audio_from_video(video_path, extracted_audio_path)
separate_voices(extracted_audio_path, separate_output_path)
```

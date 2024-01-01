# Handles converting audio files to text
from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment
import os

SUPPORTED_EXTENSIONS = ["mp3", "m4a", "flac", "wav", "wma", "aac"]


def long_running_recognize(storage_uri):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=storage_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=300)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript
        print("Raw Transcript: ")
        print(transcript)        
    return transcript

def convert_to_wav(audio_file_path):
    # Get the file extension
    file_extension = os.path.splitext(audio_file_path)[1][1:]

    # Check if the file extension is supported
    if file_extension.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file extension {file_extension}")
    
    # Create the corresponding audio segment based on the file extension
    audio = AudioSegment.from_file(audio_file_path, format=file_extension)
    
    # Make the modifications and save it as a wav file
    audio = audio.set_channels(1)  # set audio to mono
    audio = audio.set_frame_rate(16000)  # set frame rate suitable for SpeechRecognition
    wav_file_path = audio_file_path.replace("." + file_extension, ".wav")
    audio.export(wav_file_path, format="wav")
    
    return wav_file_path


if __name__ == "__main__":
    mp3_file_path = input("Please enter the path to the mp3 file: ")
    try: 
        wav_file_path = convert_to_wav(mp3_file_path)
        long_running_recognize(wav_file_path)
    except ValueError as e:
        print(e)
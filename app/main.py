import logging
import os
from audio_processing.speech_to_text import long_running_recognize, convert_to_wav
from audio_processing.cloud_storage import upload_blob
from text_processing.gpt_summary import process_transcript, chunk_transcript_by_tokens
from file_management.file_operation import write_to_file

logging.basicConfig(level=logging.DEBUG)

def get_user_input():
    mp3_file_path = input("Please enter the path to the audio file: ")
    return mp3_file_path

def main():
    mp3_file_path = get_user_input()
    logging.debug(f"Received audio file path: {mp3_file_path}")

    wav_file_path = convert_to_wav(mp3_file_path)
    logging.debug(f"Converted to WAV: {wav_file_path}")

    bucket_name = "jaar_audio_files"
    destination_blob_name = "audio_files_dest/" + wav_file_path.split("/")[-1]
    upload_blob(bucket_name, wav_file_path, destination_blob_name)
    logging.debug(f"Uploaded to GCS: {destination_blob_name}")

    audio_file_uri = f"gs://{bucket_name}/{destination_blob_name}"
    transcript = long_running_recognize(audio_file_uri)
    logging.debug(f"Received transcript: {transcript[:50]}...")

    transcript_chunks = chunk_transcript_by_tokens(transcript)
    summarized_transcripts = [process_transcript(chunk) for chunk in transcript_chunks]

    output_directory = "/Users/luke/VSCode/JaaR/transcripts/"
    output_file_name = f"{mp3_file_path.split('/')[-1].split('.')[0]}.txt"

    with open(os.path.join(output_directory, output_file_name), 'w') as outfile:
        for i, summary_list in enumerate(summarized_transcripts, start=1):
            for summary in summary_list:
                outfile.write(f'{summary}\n')
            logging.debug(f"Summary written to {output_file_name}")

if __name__ == "__main__":
    main()

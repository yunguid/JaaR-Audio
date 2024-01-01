# JaaR Audio 
![Alt text](https://github.com/yunguid/JaaR-Audio/blob/main/JaaR.png?raw=true)
JaaR is a Python-based tool that converts spoken language audio files to text and then summarizes the content using OpenAI's GPT-3.5. It utilizes Google Cloud Storage for audio file management and Google Speech-to-Text for transcription.


## Features

- Converts various audio formats to WAV
- Performs long-running speech recognition
- Uploads audio files to Google Cloud Storage (GCS)
- Summarizes transcripts using OpenAI's GPT-3.5

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- Access to Google Cloud Services and an OpenAI API key
- `ffmpeg` or `avlib` installed on your system for `pydub` processing

## Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/your-github-username/JaaR.git
cd JaaR
```
Install the required libraries: 

```pip install -r requirements.txt```

## Setup 
Set up the necessary environment variables 
```export OPENAI_API_KEY = 'your_openai_key_here'```
Make sure you have also configured Google Cloud credentials as described in the Google Cloud documentation. 

## Usage 
```python main.py```
When prompted, enter the path to the audio file you wish to process.

## Contribute to JaaR
To contribute please follow these steps: 
1. Fork this repository 
2. Create a new branch 'git checkout -b <branch_name>
3. Make your changes and commit them: git commit -m <commit_message>
4. Push to the original branch: 'git push origin <project_name>/<location>
5. Create a pull request 

## Contact 
- email: l.yng31323(at)gmail.com
- This project was intented to be an exploration of AI and audio to text conversion. I've got a lot to learn and am open to any suggestions or further discussion. I will be updating the code over time to improve functionality. 







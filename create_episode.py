from openai import OpenAI
from datetime import datetime
from pathlib import Path
import os

class Episode:
    def __init__(self, title, description, audio_file):
        self.title = title
        self.description = description
        self.audio_file = audio_file
        self.pub_date = datetime.now(tz=None).isoformat() #TODO learn how to properly tell the time
        self.length = str(type(self).get_length(audio_file))
        self.type = 'audio/mpeg'
        self.guid = f'https://tighebrary.io/daily-feed/{audio_file}'
        self.url = f'https://tighebrary.io/daily-feed/{audio_file}'

    @staticmethod
    def get_length(audio_file):
        return os.path.getsize(audio_file)

def new_episode():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Generate all elements in one request
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Search the web for today's biggest news story about New York City. Based on the news story, generate a podcast episode with a title, description, and content. The content should be written as plain text, without any special formatting, and without creating a script. The content should be a clear, compelling, and succinct summary of the news story, about 100 words long. The title and description should be related to the content."
            }
        ]
    )

    print(completion.choices[0].message.content)
    response = [line for line in completion.choices[0].message.content.split('\n') if line.strip()]
    print(response)
    title = response[0].replace("Title: ", "")
    description = response[1].replace("Description: ", "")
    audio_content = "\n".join(response[2:]).replace("Content: ", "")

    # Generate the audio file
    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=audio_content
    )

    date = datetime.now(tz=None).isoformat()
    speech_file_path = Path(__file__).parent / "audio" / "gpt" / f"{date}.mp3"
    speech_response.stream_to_file(speech_file_path)

    # Create the episode
    episode = Episode(title, description, speech_file_path)
    print(f"Episode created with title: {episode.title}, description: {episode.description}, audio file: {episode.audio_file}")
    return episode

new_episode()


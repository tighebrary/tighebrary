from openai import OpenAI
from datetime import datetime
from pathlib import Path

client = OpenAI()
date = datetime.now(tz=None).isoformat()

speech_file_path = Path(__file__).parent / "audio" / "gpt" / f"{date}.mp3"

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=completion.choices[0].message.content
)

response.stream_to_file(speech_file_path)
print(f"Audio saved to {speech_file_path}")
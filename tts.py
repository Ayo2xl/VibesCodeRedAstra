import os
from elevenlabs.client import ElevenLabs
from elevenlabs import save

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    raise SystemExit("Set the ELEVENLABS_API_KEY environment variable first.")

client = ElevenLabs(api_key=api_key)

def text_to_speech(text, voice_id="21m00Tcm4TlvDq8ikWAM", output_file="output.mp3"):
    try:
        audio = client.text_to_speech.convert(text=text, voice_id=voice_id)
        save(audio, output_file)
        print(f"Audio saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error generating speech: {e}")
        return False

if __name__ == "__main__":
    text = "Hello, this is a test of my text to speech app."
    if text_to_speech(text):
        print("Done! Check output.mp3")
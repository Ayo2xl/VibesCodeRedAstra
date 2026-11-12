import os # acces to operating systems 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY") 
from elevenlabs.client import ElevenLabs
from elevenlabs import save # helper save to help me write audio to a file.

api_key = os.environ.get("ELEVENLABS_API_KEY") # looks for the api through the environemt and
# helps store the API key securely.
if not api_key:  # if its not set 
    raise SystemExit("Set the ELEVENLABS_API_KEY environment variable first.") # raise prints the message and stops the program.

client = ElevenLabs(api_key=api_key) # creates a client objet and stores in client. The api key is used to authenticate the client.

voice = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Sam": "EXAVITQu4vr4xnSDxMaL",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
}
# This creates a dictionary of voices and their corresponding voice ids.
# This function allows the user to choose a voice from the dictionary.
def text_to_speech(text, voice_id="21m00Tcm4TlvDq8ikWAM", output_file="output.mp3"):
    try:
        audio = client.text_to_speech.convert(text=text, voice_id=voice_id) # calls speech conversion feature through the client i created.
        save(audio, output_file) # saves the generated audio to the specified output file.
        print(f"Audio saved to {output_file}")
        return True
    except Exception as e:# catches any errors that occur during speech generation.
        print(f"Error generating speech: {e}")#
        return False

def choose_voice():
    names = list(voice.keys())
    print("Choose a voice")

    for i, name in enumerate(names, start = 1): # loops through the voice names and displays them with numbers.
        #enumerate gives each name a number so user sees 1. Rachel.....
        print(f"{i}. {name}") 

    choice = input("Enter your choice: ") # allows the user to choose a voice from the dictionary.
    if not choice.isdigit() or int(choice) not in range (1, len(names) + 1):
        # checks if the user's input is a digit and within the valid range.
        raise SystemExit("Invalid choice. Please try again.")
    return voice[names[int(choice) - 1]]
# function that allows the user to choose a voice from the dictionary.
if __name__ == "__main__":
    while True:
        text = input("\nEnter text (or 'quit' to exit): ")
        if text.strip().lower() == "quit":
            print("Goodbye!")
            break
        if text.strip() == "":
            print("Please enter some text.")
        else:
            voice_id = choose_voice()
            if text_to_speech(text, voice_id=voice_id):
                print("Done! Check output.mp3")
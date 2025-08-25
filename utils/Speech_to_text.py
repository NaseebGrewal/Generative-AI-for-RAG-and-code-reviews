import os
import threading

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()


def transcribe_wav_file(file_path, subscription_key, service_region):
    # Initialize the speech configuration with the subscription key and service region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)

    # Set the input audio file to be transcribed
    audio_input = speechsdk.AudioConfig(filename=file_path)

    # Initialize the speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    # Create a threading Event object to control the stopping condition
    transcription_completed_event = threading.Event()

    transcription = []

    # Define a callback function for the speech recognizer's recognized event
    def recognized_event_handler(evt):
        print(f"{evt.result.text}")
        transcription.append(evt.result.text)

    # Define a callback function for the speech recognizer's session stopped event
    def session_stopped_event_handler(evt):
        print("Transcription completed.")
        transcription_completed_event.set()

    # Attach the recognized event handler to the speech recognizer
    speech_recognizer.recognized.connect(recognized_event_handler)

    # Attach the session stopped event handler to the speech recognizer
    speech_recognizer.session_stopped.connect(session_stopped_event_handler)

    # Start the continuous recognition process
    print("Starting transcription...")
    speech_recognizer.start_continuous_recognition()

    # Wait for the transcription to complete
    transcription_completed_event.wait()

    # Stop the continuous recognition process
    speech_recognizer.stop_continuous_recognition()
    return "\n".join(transcription)


# if __name__ == "__main__":
#     azure_subscription_key = os.environ["speech_key"]
#     azure_service_region = os.environ["speech_region"]
#     # wav_file_path = './sound_samples_files/VoiceMessage.wav'
#     wav_file_path= r"C:\Users\Legion 5 Pro 007\Documents\HM\Speech-to-text\sound_samples_files\wipe_my_mouth.wav"
#     text = transcribe_wav_file(wav_file_path, azure_subscription_key, azure_service_region)
#     # print(text)


def get_text(wav_file_path):
    azure_subscription_key = os.environ["speech_key"]
    azure_service_region = os.environ["speech_region"]

    text = transcribe_wav_file(wav_file_path, azure_subscription_key, azure_service_region)
    return text

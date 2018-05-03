####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 19th March 2018     #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################


import requests
import json
from SpeechRecording import record_audio, read_audio
from Skills.EchoSkill import echo
from playdong import playdong
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'Wit API access token'


def hear(AUDIO_FILENAME, num_seconds = 5):
  try:  
    AUDIO_FILENAME = "Audio/" + AUDIO_FILENAME + ".wav"
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
    playdong()

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    text = data['_text']
    print text
    # return the text
    return text

  except:
      echo("I could not catch that.")
      return "Error"

'''if __name__ == "__main__":
    text =  hear('myspeech.wav', 4)
    print("\nYou said: {}".format(text))'''


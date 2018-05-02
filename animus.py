####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################

# use Wit.ai for STT
# use of pyttsx for TTS -> voice.py to debug voice of the AI
# System wide voice support from the Skills/EchoSkill.py
# use of Padatious Intent Parser for Intent Parsing using Artificial
# Neural Networks
# use of aRest API for Ind System control
# import files and dependencies
# this will be the core entry point of the AI




from Skills.EchoSkill import echo
from Skills.Summarize import get_news
from Skills.WeatherSkill import weather
from Skills.MailSkill import MailSkill
from Skills.GoogleSkill import google
from Skills.Summarize import search_shorten
from Skills.JokeSkill import Joke
from Skills.GreetingSkill import Greetings
from Skills.WolframSkill import Wolfram_ask
from SpeechRecog import hear
from Skills.TimeIntent import time_now
from Skills.IndSkill import electric
from intent import determine_intent
from playding import playding
from playdong import playdong

import sys
sys.path.append('/snowboy/examples/Python')#Path to snowboy decoder package
import snowboydecoder

# obtain audio from the microphone


def animus_core():
   detector = snowboydecoder.HotwordDetector("Animus.pmdl", sensitivity=0.5, audio_gain=1)
   detector.start(detected_callback)


def detected_callback():
    print "hotword detected"
    Greetings("h")
    playding()
    request = hear("Temp", 5)
    if request == "Error": animus_core()
    intent = determine_intent(request)
    if intent.name == "time": time_now()
    elif intent.name == "Wolfram": Wolfram_ask(request)
    elif intent.name == "goodbye": Greetings("b")
    elif intent.name == "search":
         google(intent.matches["query"])

    elif intent.name == "Creator": echo("I was created by Kuldeep Paul")
    elif intent.name == "Me": echo("I am Animus, an Artificial Intelligence Program, developed to help you with boring stuff")
    elif intent.name == "weather": weather()
    elif intent.name == "Joke": Joke("j")
    elif intent.name == "lights":
         state = intent.matches["state"]
         electric("asdfgh", 0, state)

animus_core()

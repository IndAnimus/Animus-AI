####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
####################################################################
#EchoSkill.py

import pyttsx

def echo(Message):
   engine = pyttsx.init()
   engine.setProperty('rate', 125)
   engine.setProperty('volume', 5)
   engine.setProperty('voice', 1)
   print(Message)
   engine.say(Message) 
   engine.runAndWait()
   return 0

   
######################################################################
#System wide voice implementation through the echo skill in Animus AI#
#Copyright Kuldeep Paul                                              #
######################################################################

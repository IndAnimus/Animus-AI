####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
####################################################################
'''

   THIS PROGRAM IS INTENDED FOR USE UNDER SUPERVISION OF HUMAN
   INTERVENTION. THE SKILL ADDS CAPABILITY OF SCANNING AND ACCESSING 
   DEVICES ON THE NETWORK. NEITHER THE CREATOR OR THE DEVELOPERS OF 
   ANIMUS AI ARE RESPONSIBLE FOR MISUSE OF THIS CODE FOR MALITIOUS 
   PURPOSES. ANIMUS AI HAS THE CAPABILITY TO SCAN FOR DEVICES ON THE 
   NETWORK TO ENABLE IT TO INTERACT WITH OTHER DEVICES. PLEASE USE
   WISELY AND AT YOUR OWN DISCRETION.

'''
#GoogleSkill.py

from Summarize import search_shorten
from EchoSkill import echo
import sys
sys.path.append('/home/kuldeep/snowboy/examples/Python')
import snowboydecoder

def google(search):
   echo("Sir, I am Searching Google for " + search)
   from googlesearch.googlesearch import GoogleSearch
   response = GoogleSearch().search(search, num_results = 2)
   detector = snowboydecoder.HotwordDetector("Animus.pmdl", sensitivity=0.5, audio_gain=1)
   detector.start(back)
   for result in response.results:
       echo("Title: " + result.title)
       search_shorten(result.getText())
      # echo("Content: " + result.getText())
   return 0
def back():
   return 0

######################################################################
#System wide google search implementation through the google skill in#
#Animus AI                                                           #
#Copyright Kuldeep Paul                                              #
######################################################################

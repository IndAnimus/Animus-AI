
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
#    Animus Wolfram Alpha Skill for Responses                      #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################
import wolframalpha
from EchoSkill import echo



def Wolfram_ask(query):
  try:
   client = wolframalpha.Client("Your API Key")
   res = client.query(query)
   print query
   echo(next(res.results).text)
   
  except:
   echo("Please re-phrase your request.")
  return 0

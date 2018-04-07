####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
####################################################################
####################################################################
####################################################################
#******************************************************************#
#                 Voice Debugger Animus AI v.1.0                   #
####################################################################
import pyttsx
voiceEngine = pyttsx.init()

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
 
print rate
print volume
print voice

newVoiceRate = 100
while newVoiceRate <= 300:      ###loop implementation
    voiceEngine.setProperty('rate', newVoiceRate)
    voiceEngine.say('Testing different voice rates.')
    voiceEngine.runAndWait()
    newVoiceRate = newVoiceRate+5
 
voiceEngine.setProperty('rate', 125)
#normal implementation 
newVolume = 5
newVoice = 1
voiceEngine.setProperty('volume', newVolume)
voiceEngine.setProperty('voice', newVoice)
voiceEngine.say('Testing different voice volumes.')
voiceEngine.runAndWait()
print(newVolume)
newVolume = newVolume+1

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
 
print rate
print volume
print voice
######################################################################
#Voice Debugger in Animus AI                                         #
#Copyright Kuldeep Paul                                              #
######################################################################



#!usr/bin/env python  
#coding=utf-8  
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################

import pyaudio  
import wave  

#define stream chunk   
chunk = 1024  
def playdong():
   #open a wav format music  
   f = wave.open(r"/home/kuldeep/Desktop/ANIMUS/dong.wav","rb")  
   #instantiate PyAudio  
   p = pyaudio.PyAudio()  
   #open stream  
   stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
   #read data  
   data = f.readframes(chunk)  

   #play stream  
   while data:  
       stream.write(data)  
       data = f.readframes(chunk)  

   #stop stream  
   stream.stop_stream()  
   stream.close()  

   #close PyAudio  
   p.terminate()  

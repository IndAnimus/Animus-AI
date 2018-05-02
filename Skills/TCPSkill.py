#!/usr/bin/env python
# -*- coding: utf-8 -*-
#######################################################
# ANIMUS AI TCP/IP Scanner Ported from Github with    #
# necessary changes in code.                          #
#######################################################
'''
call method:
            ScanForDevices in 10.30.0.x range => ScanForDevices(10.30.0)
''' 
import os
import time

from subprocess import Popen

def ScanForDevices(ip_araligi_deger):
   import os
   devnull = open(os.devnull, 'wb')

   star = "**********************************************************************"

  # ip_araligi_deger = "10.30.32" #IP Address
   print "Scanning IP Range:",ip_araligi_deger 

   print star

   if ip_araligi_deger == "":
    print star
    print "Try Valid IP Range..."
    print star

   import sys

   p = []
   aktif = 0
   yanit_yok = 0
   pasif = 0

   for aralik in range(0,255):
      ip = ip_araligi_deger + ".%d" %aralik
      p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
   while p:
       for i, (ip, proc) in enumerate(p[:]):
           if proc.poll() is not None:
               p.remove((ip, proc))
               if proc.returncode == 0:
                   print('%s Active' % ip)
                   aktif = aktif + 1
               elif proc.returncode == 2:
                   print('%s No Answer' % ip)
                   aktif = yanit_yok + 1
               else:
                   print('%s Passive' % ip)
                   pasif = pasif + 1
       time.sleep(.04)
   devnull.close()

   print star

   print "LOCAL NETWORK IP SCANNER."

   print star

   import os

   print "Current operating system",os.name
   print "Network Status"
   print "Active IP  [ ",aktif," ]"
   print "Passive IP [ ",pasif," ]"
   print "No Answer  [ ",yanit_yok," ]"

   print star

   bitis_mesaj = "Scan Complete"

   print bitis_mesaj

   print star
   return 0
#ScanForDevices("10.30.0")

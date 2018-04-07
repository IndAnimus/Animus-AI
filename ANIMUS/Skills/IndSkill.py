import urllib
def electric(device_name, pin, gamma):
   try:
      if gamma == "on":
         pin_state = 0
         access = "https://cloud.arest.io/" + device_name + "/mode/" + pin+"/o"
         state = "https://cloud.arest.io/" + device_name + "/digital/" + pin+"/"+ pin_state
         urllib.urlopen(access)
         urllib.urlopen(state)
      else:
         pin_state = 1
         state = "https://cloud.arest.io/" + device_name + "/digital/" + pin+"/"+ pin_state
         urllib.urlopen(state)

      return 0

   except:
      print "Error"
      return 0


   


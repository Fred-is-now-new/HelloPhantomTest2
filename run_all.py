import sys
import datetime
from playsound3 import playsound

import RPi.GPIO as GPIO
import time

#print(sys.path)

sys.path.append('/home/mbachek/Desktop/HelloPhantom/environment')
#print(sys.path)

from stt import *
from recognizer import *
from webscraper import *
from tts import *
#from client import send

inputText = stt.voskRecognize()
print("Text Input: " + inputText)

computed = logic(inputText)
print("Logic output:")
print(computed)


if computed[0] == "today":
	day = datetime.date.today()
elif computed[0] == "tomorrow":
	day = datetime.date.today() + datetime.timedelta(days=1)
elif computed[0] == "yesterday":
	day = datetime.date.today() - datetime.timedelta(days=1)
else:
	day = datetime.date.today()
	
print("Calculated date: " + str(day))


#result = webscrape(computed[1], str(day))
#sorry, I wanted to test code in a new way, i can fix formatting -Shlok
result = webscrape(computed[1], computed[0])
#print("Transcript:\n" + result)
print(result)

speak(str(result))

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.output(17,GPIO.HIGH)
time.sleep(5)
GPIO.output(17,GPIO.LOW)

GPIO.cleanup()

playsound("/home/mbachek/Desktop/HelloPhantom/!environment/output.mp3")
print("Program completed")


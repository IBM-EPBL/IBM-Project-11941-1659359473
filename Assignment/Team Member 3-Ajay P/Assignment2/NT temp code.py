import datetime
import time
import random
import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BCM)      
GPIO.setwarning(false)     
BUZZER = 23                
buzzerstate = False 

now = datetime.datetime.now()
GPIO.setup(BUZZER,GPIO.OUT)


while True:
    temperature = random.randint(0, 100)
    humidity = random.randint(0, 100)
    buzzstate = not buzzstate                
	GPIO.output(BUZZER,buzzstate)
    if(temperature>=50 or humidity>=50):      
	print("Threshold temperature/humidity crossed limit on",now.strftime("%d-%m-%y"),"at",now.strftime("%H:%M"))
	time.sleep(1)

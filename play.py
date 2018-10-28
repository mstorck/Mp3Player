#!/usr/bin/python

import os
import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
os.system('mpg123 /home/pi/Mp3Player-master/system.mp3')

while True:

      if GPIO.input(17) ==0:

            print ("Pulse")
		GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
            os.system('/home/pi/Mp3Player-master/mp3.sh')
            GPIO.setup(23, GPIO.IN)
            GPIO.setup(24, GPIO.IN)
            time.sleep(1)

      time.sleep(0.5)

GPIO.cleanup()

# Mp3Player
Based on raspberry pi. If you close the contact on the GPIO17, it plays one song randomly from a USB stick

It runs on python 3.5 (and apparently on python 2.7.9)

all the mp3's have to be on an usb stick with a directory named mp3

you can trigger a relay via GPIO.BCM23 and GPIO.BCM24, GPIO.HIGH while MP3 is playing, GPIO.LOW otherwise.

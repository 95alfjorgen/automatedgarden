#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime, time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 4, 17]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)



    light = 2

    IO.setup(light, GPIO.OUT)

    while(True):
        now = datetime.datetime.now()
        startTime = now.replace(hour=8, minute=0, second=0, microsecond=0)
        stopTime = now.replace(hour=18, minute=0, second=0, microsecond=0)
        onPeriod = now > startTime and now < stopTime
        
        if onPeriod:
            IO.output(light, True)
        else:
            IO.output(light, False)
        
        #Tar pause på 60 sekund. Koden kjorer derfor en gang i minuttet. (da krasjer det heller ikke)
        time.sleep(60) 
main()

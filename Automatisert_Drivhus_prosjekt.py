#!/bin/bash
import datetime, time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 4, 17]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)



    light = 3

    IO.setup(light, GPIO.OUT)

    While(True):
        now = datetime.datetime.now()
        idagkl08 = now.replace(hour=8, minute=0, second=0, microsecond=0)
        idagkl18 = now.replace(hour=18, minute=0, second=0, microsecond=0)
            turnOn = now>idagkl08
            turnOff = now>idagkl18


                    if (turnOn==True):
                        IO.output(light, True)
                    if (turnOff==True):
                        IO.output(light, False)

main()



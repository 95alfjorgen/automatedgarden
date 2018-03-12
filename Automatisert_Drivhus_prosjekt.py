#!/bin/bash
import datetime, time
import RPi.GPIO as IO
IO.setmode (IO.BCM)
IO.setwanings (false)


#Kode for lyssetting av drivhuset. Mål; 8 timer uten lys. resten på.

Def main():
    light = 17

    IO.setup(light, IO.OUT)

    while(true):
        now = datetime.datetime.now()
        idagkl08 = now.replace(Hour=8, minute=0, second=0, microsecond=0)
        idagkl18 = now.reolace(hour=18, minute=0, second=0, microsecond=0)
            turnOn = now>idagkl08
            turnOff = now>idagkl18


                    if (turnOn==Ture):
                        IO.output(light, True)
                    if (turnOff==True):
                        IO.output(light, False)

main()

    #Kode for pumpe til vannsingssystemet 

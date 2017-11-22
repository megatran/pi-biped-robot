
Conversation opened. 1 read message.

Skip to content
Using Colorado School of Mines Mail with screen readers
Search



Mail
COMPOSE
Labels
Inbox (2)
Starred
Sent Mail
Drafts (5)
More 
Hangouts

 
 
 
  More 
1 of 5,044  
 
Print all In new window
py 
Inbox
x 

Arthur Mayer <arthurmayer@mymail.mines.edu>
Attachments9:24 PM (4 minutes ago)

to me 
2 Attachments 
 
	
Click here to Reply or Forward
Using 0.63 GB
Program Policies
Powered by Google
Last account activity: 0 minutes ago
Open in 1 other location  Details


import RPi.GPIO as GPIO
import time
import numpy
import spidev
import RPi.GPIO

buzzerPin=17

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(buzzerPin, RPi.GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 10000000

def readAdc (channel):
    r = spi.xfer2([int('0110000',2), 15])
    s = bin(r[0])[2:].zfill(10)
    data = int(s[8:] + '0'*8, 2) + r[1]
    #print (r, s)
    return data

def buzz(pitch, duration):
    period = 1.0/(pitch+1)
    delay = period/2
    cycles = int(duration*pitch)

    for i in range(cycles):
        RPi.GPIO.output(buzzerPin, True)
        time.sleep(delay)
        RPi.GPIO.output(buzzerPin, False)
        time.sleep(delay)

    time.sleep(duration*0.3)

# Advantage is we can change the port only in this line and all the references below will get updated to that port instead of changing the port number at every single line.
trigPin=23
echoPin=21

GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(trigPin, GPIO.OUT)
pulse_start=0
pulse_end=0

try:
    time.sleep(5)
    buzz(float(2000), float(.6))
    print("Measuring")
    while True:
        GPIO.output(trigPin, True)
        time.sleep(0.0001)
        GPIO.output(trigPin, False)
        
        while GPIO.input(echoPin)==0:
            pulse_start=time.time()
        while GPIO.input(echoPin)==1:
            pulse_end=time.time()
            #print("HI")
        pulse_duration=pulse_end-pulse_start
        distance=round(pulse_duration*17150, 2)
        print(distance)
        if (distance<5):
            print("WALL!")
            buzz(float(1500), float(.3))
        #print("Distance:"+ str(distance) + "cm")
except KeyboardInterrupt:    
    GPIO.output(trigPin, False)
    GPIO.cleanup()    
test_ultrasonic.py
Open with
Displaying test_ultrasonic.py.

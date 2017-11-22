import RPi.GPIO as GPIO
import time

# Advantage is we can change the port only in this line and all the references below will get updated to that port instead of changing the port number at every single line.
trigPin=23
echoPin=21
GPIO.setmode(GPIO.BCM) #set pinmode to use number on board

GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(trigPin, GPIO.OUT)
pulse_start=0
pulse_end=0

try:
    time.sleep(5)
    print("Measuring")
    while True:
        GPIO.output(trigPin, True)
        time.sleep(0.0001)
        GPIO.output(trigPin, False)
        
        while GPIO.input(echoPin)==0:
            pulse_start=time.time()
        while GPIO.input(echoPin)==1:
            pulse_end=time.time()
            print("HI")
        pulse_duration=pulse_end-pulse_start
        distance=round(pulse_duration*17150, 2)
        
        print("Distance:"+ str(distance) + "cm")
except KeyboardInterrupt:    
    GPIO.output(trigPin, False)
    GPIO.cleanup()

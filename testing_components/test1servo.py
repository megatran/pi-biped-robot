import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23,50)

p.start(7.5)

try:
        
        while True:
                
                print("90 deg")
                p.ChangeDutyCycle(7.5) #turn towards 90 degre. CENTER
                time.sleep(2) # sleep 1sec
                print("0 deg")
                p.ChangeDutyCycle(2.5) #turn towards 0 degree
                time.sleep(2)
                print("180 deg")
                p.ChangeDutyCycle(12.5) #turn towards 180 degree
                time.sleep(2)
                
                print("0 deg again")
                p.ChangeDutyCycle(7.5)
                time.sleep(2)
                print("4.5% CCW")
                p.ChangeDutyCycle(4.5)
                time.sleep(2)
                print("10.5% CW")
                p.ChangeDutyCycle(10.5)
                time.sleep(2)
                
        

except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()


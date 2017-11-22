import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

try:
    while (1):
        
        p1 = GPIO.PWM(18, 50)
        p2 = GPIO.PWM(19, 50)
        p3 = GPIO.PWM(20, 50)
        p4 = GPIO.PWM(21, 50)
        p5 = GPIO.PWM(22, 50)

        p1.start(12.5)#Turn 4 degrees per cycle. 15 cycles = 60 degrees.
        p2.start(12.5)
        p3.start(12.5)
        p4.start(12.5)
        p5.start(12.5)
        s_one = 12.5
        a_one = 10.5

        # Make servo move slowly from 180 angle position to 144 deg and stop at 144 deg
        '''while s_one >= a_one:
            p1.ChangeDutyCycle(s_one)
            p2.ChangeDutyCycle(s_one)
            p3.ChangeDutyCycle(s_one)
            p4.ChangeDutyCycle(s_one)
            p5.ChangeDutyCycle(s_one)
            time.sleep(0.2)
            s_one -= 0.5'''

        print(s_one)
except (KeyboardInterrupt, SystemExit):
    print("EXITING")
    GPIO.cleanup()
    

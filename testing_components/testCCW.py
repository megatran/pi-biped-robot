import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT)

pwm = GPIO.PWM(24,50)        #sets pin 21 to PWM and sends 50 signals per second

pwm.start(0)          #starts by sending a pulse at 7.5% to center the servo

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(24, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(24, False)
	pwm.ChangeDutyCycle(0)

try:                
    """
    while True:       #starts an infinite loop
        p.ChangeDutyCycle(1)                   # change duty cycle for getting the servo position to 90º
        time.sleep(0.2)                                      # sleep for 1 second
        #p.ChangeDutyCycle(12.5)                  # change duty cycle for getting the servo position to 180º
        #time.sleep(0.2)                                     # sleep for 1 second
        #p.ChangeDutyCycle(2.5)                  # change duty cycle for getting the servo position to 0º
        #time.sleep(0.2)                                     # sleep for 1 second      
        break
        """
    SetAngle(45)
    GPIO.cleanup()
except KeyboardInterrupt:

    p.stop()

    GPIO.cleanup()                 #supposed to stop when a key is pressed, doesn’t work


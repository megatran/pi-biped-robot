import RPi.GPIO as GPIO
import time 


GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT) # balancer
#GPIO.setup(24,GPIO.OUT) # left leg
#GPIO.setup(20,GPIO.OUT) # left knee
#GPIO.setup(21,GPIO.OUT) # right leg
#GPIO.setup(22,GPIO.OUT) # right_knee
try:
    while(1):
        balancer=GPIO.PWM(19,50)
        #left_leg=GPIO.PWM(24,50) 
        #left_knee=GPIO.PWM(20,50)
        #right_leg=GPIO.PWM(21,50)
        #right_knee=GPIO.PWM(22,50)
        #test=5.0

        #left_leg.start(5)
        #left_knee.start(5)
        #right_leg.start(5)
        #balancer.ChangeDutyCycle(5)
        #right_knee.start(5)
        #right_leg.ChangeDutyCycle(5)
        #left_leg.ChangeDutyCycle(7)
        #left_knee.ChangeDutyCycle(4)
        time.sleep(1)


        s_one = 10.5
        a_one = 10.0
        balancer.start(s_one)
        while s_one >= a_one:

            balancer.start(s_one)

            balancer.ChangeDutyCycle(s_one)
            
            time.sleep(0.2)
            balancer.stop()
            time.sleep(1)
            

            print(s_one)
            s_one -= 0.5
        print("done")

        
        break
        GPIO.cleanup()


except (KeyboardInterrupt, SystemExit):
    print("EXITING")
    GPIO.cleanup()
    GPIO.cleanup()

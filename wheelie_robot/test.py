import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

# use pwm to run gpio pins at 50% duty cycle
p = GPIO.PWM(10, 20)  # frequency to 20
q = GPIO.PWM(9, 20)  # frequency to 20
p.start(50)
q.start(0)
time.sleep(5)
GPIO.output(10, 0)
GPIO.output(9, 0)
GPIO.cleanup()

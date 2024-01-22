import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

class Motor:
    def __init__(self, pinFwd, pinBack, frequency=20, maxSpeed=100):
        self.pinFwd = pinFwd
        self.pinBack = pinBack
        self.maxSpeed = maxSpeed
        self.frequency = frequency
        
        GPIO.setup(self.pinFwd, GPIO.OUT)
        GPIO.setup(self.pinBack, GPIO.OUT)
        self.pwm1 = GPIO.PWM(self.pinFwd, frequency)
        self.pwm2 = GPIO.PWM(self.pinBack, frequency)
        self.pwm1.start(0)
        self.pwm2.start(0)

    def move(self, speed):
        if speed > self.maxSpeed:
            speed = 100
        elif speed < -100:
            speed = -100
        
        if speed > 0:
            self.pwm1.ChangeDutyCycle(speed)
            self.pwm2.ChangeDutyCycle(0)
        elif speed == 0:
            self.pwm1.ChangeDutyCycle(0)
            self.pwm2.ChangeDutyCycle(0)
        else:
            self.pwm1.ChangeDutyCycle(0)
            self.pwm2.ChangeDutyCycle(-speed)

    def stop(self):
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)

class Wheelie:
    def __init__(self):
        self.leftMotor = Motor(10, 9)
        self.rightMotor = Motor(8, 7)
        
        self.leftMotor.move(0)
        self.rightMotor.move(0)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()

    def turnLeft(self, speed=50):
        self.leftMotor.move(-speed)
        self.rightMotor.move(speed)

    def turnRight(self, speed=50):
        self.leftMotor.move(speed)
        self.rightMotor.move(-speed)

    def forward(self, speed=50):
        self.leftMotor.move(speed)
        self.rightMotor.move(speed)

    def backward(self, speed=50):
        self.leftMotor.move(-speed)
        self.rightMotor.move(-speed)

def main():
    wheelie = Wheelie()
    wheelie.forward()
    time.sleep(1)
    wheelie.turnLeft()
    time.sleep(1)
    wheelie.backward(50)
    time.sleep(1)
    wheelie.turnRight()
    time.sleep(1)
    wheelie.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
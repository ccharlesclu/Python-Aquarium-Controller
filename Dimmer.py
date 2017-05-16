import RPi.GPIO as GPIO

class Dimmer:
    def __init__(self,pin):
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 1000)
        self.pwm.start(0.0)

    def set(self,value):
        self.pwm.ChangeDutyCycle(value)

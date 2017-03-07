import RPi.GPIO as GPIO
from time import sleep

class LEDControl():
    """
    LED Control

    Flashes an LED 5 times when a button is pressed.

    Args:
        _pin_in : int - input pin from button
        _pin_out : int - output pin to LED
    """

    def __init__(self, pin_in, pin_out):
        self._pin_in = pin_in
        self._pin_out = pin_out
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin_in, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self._pin_out, GPIO.OUT)
        GPIO.output(self._pin_out, False)
        GPIO.add_event_detect(self._pin_in, GPIO.FALLING, callback=self.light_LED, bouncetime=300)

    def light_LED(self, time):
        i = 1
        while i <= 5:
            GPIO.output(self._pin_out, True)
            print('LED on')
            sleep(0.5)
            print('Slept for 0.5 seconds')
            GPIO.output(self._pin_out, False)
            print('LED off')
            sleep(0.5)
            print('Slept again for 0.5 seconds')
            i = i + 1

if __name__ == "__main__":
    test_led = LEDControl(19, 16)
    while True:
        print('Waiting for 1 minute.')
        sleep(1)
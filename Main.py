import RPi.GPIO as GPIO
import time


class LEDControl()
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
        self.detect_press()
        GPIO.setup(self._pin_in, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self._pin_out, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

    def detect_press(self):
        try:
            GPIO.wait_for_edge(self._pin_in, GPIO.FALLING)
            light_LED(5)
            return void
    def light_LED(self, time):
        i = 1
        while i <=5:
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.5)
            i = i+1

if __name__ = "__main__":
    test_led = Main(19, 16)
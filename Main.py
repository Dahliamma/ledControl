import RPi.GPIO as GPIO
import time

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
        self.detect_press()
        GPIO.setmode(self._pin_in, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setmode(self._pin_out, GPIO.OUT)

    def light_LED(self, time):
        i = 1
        while i <= 5:
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.5)
            i = i + 1

    def detect_press(self):
        try:
            GPIO.wait_for_edge(self._pin_in, GPIO.FALLING)
            self.light_LED(5)
        except:
            pass

if __name__ == "__main__":
    test_led = LEDControl(19, 16)
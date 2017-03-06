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
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin_in, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self._pin_out, GPIO.OUT)
        self.detect_press()

    def light_LED(self, time):
        i = 1
        while i <= 5:
            GPIO.output(16, GPIO.HIGH)
            print('LED on')
            time.sleep(1)
            print('Slept for 0.5 seconds')
            GPIO.output(16, GPIO.LOW)
            print('LED off')
            time.sleep(1)
            print('Slept again for 0.5 seconds')
            i = i + 1

    def detect_press(self):
        try:
            GPIO.wait_for_edge(self._pin_in, GPIO.FALLING)
            self.light_LED(5)
        except:
            pass

if __name__ == "__main__":
    test_led = LEDControl(19, 16)
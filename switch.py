from threading import Thread
import time
import RPi.GPIO as GPIO

POLL_FREQUENCY = .1

class Switch:
    def __init__(self, pin, callback):
        self.callback = callback
        self.pin = pin
        self.start(pin, callback)
        self.thread = None

    def start(self, pin, callback):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.IN)
            self.thread = Thread(target=self.poll, args=())
            self.thread.start()
        except Exception as e:
            print e

    def poll(self):
        print "Starting Switch"
        while True:
            time.sleep(POLL_FREQUENCY)
            val = GPIO.input(self.pin)
            self.callback(self, val)

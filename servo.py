from threading import Thread
import time
import RPi.GPIO as GPIO

POLL_FREQUENCY = .05
FULL_SPEED = 10

class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.should_spin = [0, "left"]
        self.start()
        print "servo started"

    def start(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            self.thread = Thread(target=self.run, args=())
            self.thread.start()
            # thread.start_new_thread(self.run, ())
        except Exception as e:
            print e

    def run(self):
        print "Activating Servo"
        while True:
            while self.should_spin[0] == 0:
                time.sleep(POLL_FREQUENCY)
            self.pwm = GPIO.PWM(self.pin, 1000)
	    self.pwm.start(0)
	    if self.should_spin[1] == "left":
	        self.pwm.ChangeDutyCycle(8)
            elif self.should_spin[1] == "right":
		self.pwm.ChangeDutyCycle(62)	
            else:
                self.pwm.ChangeDutyCycle(5)
            while self.should_spin[0] > 0:
		print "spinning" + self.should_spin[1]
            	time.sleep(POLL_FREQUENCY)
                self.should_spin[0] -= 1
            self.pwm.stop()

    def spin(self, direction, time):
        self.should_spin = [time, direction]

    def stop(self):
        self.should_spin = [0, "left"]
s = Servo(3)
s.spin("hi", 100)

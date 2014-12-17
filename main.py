import switch
import servo
import vision

import thread
import time

SLEEP_PERIOD = .05

# States
WAITING = 1
BALL_FOUND = 2
DOG_FOUND = 3

class Robot:
    def __init__(self):
        # TODO add the correct pin numbers here
        self.state = WAITING
        self.dog_location = None
        self.hammer_servo = servo.Servo(27)
        print "hammer started"
        self.base_servo = servo.Servo(22)
        print "base started"
        self.switch = switch.Switch(11, self.switch_triggered)
        print "switch started"
        self.dog_detector = vision.Detector(self.dog_found)
    def switch_triggered(self, sender, value):
        if value == 1:
            print "ball faound"
            self.state = BALL_FOUND

    def dog_found(self, location):
        print location
        self.dog_location = location
        if self.state == BALL_FOUND:
            self.state = DOG_FOUND

    def original_location(self):
        return self._original_location


    def throw_location(self):
        throw_location = "left" if self.dog_location == "right" else "right"
        self._original_location = self.dog_location
        return throw_location

    def run(self):
        while True:
            print "CURRENT STATE IS " + str(self.state)
            time.sleep(SLEEP_PERIOD)
            if self.state == DOG_FOUND:
                self.base_servo.spin(self.throw_location(), 10)
		time.sleep(5)
                self.hammer_servo.spin("hammer", 33)
		time.sleep(5)
                self.base_servo.spin(self.original_location(), 10)
                time.sleep(5)
                self.state = WAITING

def main():
    print "Starting robot"
    robot = Robot()
    robot.run()

main()


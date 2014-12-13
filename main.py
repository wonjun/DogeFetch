import switch
import servo
import vision

import thread
import time

class MainState(Enum):
    waiting = 1
    dog_detection = 2
    throwing = 3

class StateMachine:
    def __init__(self):
        self.state = MainState.waiting

class Robot:
    # TODO add state machine to robot
    def __init__(self):
        # TODO add the correct pin numbers here
        self.state = MainState.waiting
        self.left_servo = servo.Servo(0)
        self.right_servo = servo.Servo(0)
        self.top_servo = servo.Servo(0)
        self.switch = switch.Switch(0, self.switch_triggered)

    def switch_triggered(sender, value):
        print "switch callback called"

    def run():
        pass

def main():
    switch = switch.Switch()
    left_servo = servo.Servo()
    top_servo = servo.Servo()
    right_servo = servo.Servo()

if __name__ == "__main__":
    side_servos = [servo.Servo(), servo.Servo()]
    robot = Robot()
    main()

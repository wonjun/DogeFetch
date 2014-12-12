import switch
import servo
import vision


class Robot:
    # TODO add state machine to robot
    def __init__(self):
        # TODO add the correct pin numbers here
        self.left_servo = servo.Servo(0)
        self.right_servo = servo.Servo(0)
        self.top_servo = servo.Servo(0)
        self.switch = switch.Switch(0, self.switch_triggered)

    def switch_triggered(sender, value):
        print "switch callback called"


def main():
    switch = switch.Switch()
    left_servo = servo.Servo()
    top_servo = servo.Servo()
    right_servo = servo.Servo()

if __name__ == "__main__":
    side_servos = [servo.Servo(), servo.Servo()]
    robot = Robot()
    main()

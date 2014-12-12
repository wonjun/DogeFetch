# DogeFetch

Team: Jessica Lin, Varun Rau, Wonjun Jeong
EECS 149/249A Project Charter, Fall 2014

### Project Goal
This project will create an automated dog toy that keeps a dog entertained on its own by throwing balls in the opposite direction of the dog.

### Project Approach
The project will use a state machine governed by two main sensor inputs - a sensor for detecting whether a tennis ball has been inserted and a sensor for detecting the position of the dog relative to the robot. The goal will be to detect the insertion of a ball, detect the location of the dog, and throw the ball in the opposite direction of the dog. It would remain inert until the next tennis ball insertion.

### Resources
Our plan is to use the Arduino Uno as the processor core driving the robot’s movements. We will plan on using this to interface with a [Vernier Sensor Motion Detector](https://www.sparkfun.com/products/12875) that will be able to detect the movement and position of the dog. For detecting the insertion of the tennis ball, we plan on using a [Flexiforce Pressure Sensor](https://www.sparkfun.com/products/12875 ) to detect the weight of the inserted ball. The launching device will be able to rotate using a [Digital Continuous Rotation Servo](https://www.sparkfun.com/products/12875 ) that will rotate to the opposite direction of the dog, at which point a switch will activate the launch of the ball.

### Schedule
* October 21: Project charter due
* October 28: Statecharts simulation model with logic and timing for controller
* November 4: Project review with GSI
* November 11: Installed software for development, basic servo control
* November 17: Mini project update: demonstrate motion detection and servo control
* November 25: Motion detection of dog should activate rotation to opposite direction
* December 2: Actuation in response to ball insertion, timing of actions measured
* December 9: System testing, measure false positives, assess timing effectiveness
* December 16: Demonstration video made, powerpoint prepared
* December 17: Final presentation and demo
* December 19: Project report and video turned in

### Risk and Feasibility
The motion detector could detect ambient motion. The robot could be destroyed by dog.

### Technical Specifications
Our code is split up into several logical units.
__main.py__ contains the main run loop of our application and manages the state of the robot.
__vision.py__ contains our algorithm dog detection. It contains a continuous run loop that access the camera feed of the Microsoft Kinect.
__servo.py__ contains all the utilites necessary to operate the various rotation servos that we plan to use.
__switch.py__ contains all the utilities necessary to operate the switch that we plan to use for ball detection.

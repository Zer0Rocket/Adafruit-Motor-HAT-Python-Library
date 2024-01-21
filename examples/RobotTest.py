#!/usr/bin/python3
import time
import Robot

LEFT_TRIM = 0
RIGHT_TRIM = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

robot.forward(150, 1.0)
robot.left(200, 0.5)
robot.forward(150, 1.0)
robot.left(200, 0.5)
robot.forward(150, 1.0)
robot.left(200, 0.5)
robot.forward(150, 1.0)
robot.right(200, 0.5)

robot.right(100)
time.sleep(2.0)
robot.stop()

robot.backward(150, 1.0)
robot.right(200, 0.5)
robot.backward(150, 1.0)
robot.right(200, 0.5)
robot.backward(150, 1.0)
robot.right(200, 0.5)
robot.backward(150, 1.0)

robot.stop()

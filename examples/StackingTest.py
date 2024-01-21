#!/usr/bin/python3
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
import atexit
import threading
import random

bottomhat = Adafruit_MotorHAT(addr=0x60)
tophat = Adafruit_MotorHAT(addr=0x61)

stepperThreads = [threading.Thread(), threading.Thread(), threading.Thread()]

def turnOffMotors():
    tophat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = bottomhat.getStepper(200, 1)
myStepper2 = bottomhat.getStepper(200, 2)
myStepper3 = tophat.getStepper(200, 1)

myStepper1.setSpeed(60)
myStepper2.setSpeed(30)
myStepper3.setSpeed(15)

myMotor = tophat.getMotor(3)
myMotor.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD)

stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE]
steppers = [myStepper1, myStepper2, myStepper3]

def stepper_worker(stepper, numsteps, direction, style):
    stepper.step(numsteps, direction, style)

while True:
    for i in range(3):
        if not stepperThreads[i].isAlive():
            randomdir = random.randint(0, 1)
            print("Stepper %d" % i, end=' ')
            if randomdir == 0:
                dir = Adafruit_MotorHAT.FORWARD
                print("forward", end=' ')
            else:
                dir = Adafruit_MotorHAT.BACKWARD
                print("backward", end=' ')
            randomsteps = random.randint(10, 50)
            print("%d steps" % randomsteps)
            stepperThreads[i] = threading.Thread(target=stepper_worker, args=(steppers[i], randomsteps, dir, stepstyles[random.randint(0, len(stepstyles) - 1)],))
            stepperThreads[i].start()

            myMotor.setSpeed(random.randint(0, 255))

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import UltrasonicSensor
from pybricks.tools import wait, StopWatch
from pybricks.ev3devices import GyroSensor
from fork import Fork
from warehouse import WH
import math


class Move:
    def __init__(self):
        self.degreetoCm = 0.025
        self.wd = 55.5 
        self.timer = StopWatch()
        self.boxsize = 35
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.A)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=125)
        self.fork=Fork()
        self.my_WH = WH()
        self.gs=GyroSensor(Port.S4)            
        self.gs.reset_angle(0)
        self.mysensor = UltrasonicSensor(Port.S3)
        self.cordinates = [0]
    
    def moveforward(self, distanceinCm):
        self.robot.straight(distanceinCm)
    
    def tourn(self, degree):
        self.robot.turn((degree-self.gs.angle())-15)
        while True:
            self.robot.turn(degree-self.gs.angle())
            if degree - 1 < self.gs.angle() < degree + 1:
                break

    def backmovfrombox(self):
        self.robot.straight(self.timer.time * -100)

    def movetoWH(self):
        self.moveforward(700)
    
    def rollback(self,tavolsag):
        self.robot.straight(tavolsag)
        tourn(-90)
        self.robot.drive(100,50)
        while True:
            if mysensor.distance()<115:
                self.robot.stop
        self.fork.lift()
        self.robot.straight(-800)
        tourn(90)
    
    def movetocord(self,x,color):
        if x > self.cordinates[0]:
            tourn(-90)
            self.robot.straight((x-self.cordinates[0])*self.boxsize)
            tourn(90)

    def colorcheck(self,szin):
        change = False
        self.robot.straight(50)
        if self.fork.colorcheck(szin):
            self.fork.lift
            change = True
        else :
            self.my_WH.setboxcolor(x,szin)
        self.robot.straight(-100)
        return change

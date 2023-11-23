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
        self.cordinates = 0
        self.valami = True
    
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
        self.moveforward(600)
    
    def rollback(self,tavolsag):
        
        self.robot.straight(tavolsag*-1)
        self.tourn(-90)
        if self.valami:
            self.fork.movetolevel(1)
            self.valami = False
        else :
            self.fork.movetolevel(0)
        mehet = True
        while mehet:
            self.robot.straight(20)
            if self.mysensor.distance()<115:
                mehet = False
        self.fork.lift()
        self.robot.straight(-600)
        self.tourn(0)
        self.fork.movetolevel(0)
    
    def movetocord(self,x,color):
        if x > self.cordinates:
            self.tourn(-90)
            self.robot.straight((x-self.cordinates)*self.boxsize)
            self.tourn(0)


    def colorcheck(self,x,szin):
        change = False
        self.robot.straight(60)
        if self.fork.colorcheck(szin):
            wait(500)
            self.fork.lift()
            change = True
        else :
            self.my_WH.setboxcolor(x,szin)
        self.robot.straight(-60)
        return change

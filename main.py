#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor,  ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from fork import Fork
from warehouse import WH
from move import Move
import time

ev3 = EV3Brick()
def tourn(degree):
    robot.turn((degree-gs.angle())-15)
    for x in  range(10):
        robot.turn((degree-gs.angle())/2)


#A két kerék összekapcsolása
left_motor= Motor(Port.B)
right_motor= Motor(Port.A)
robot = DriveBase(left_motor,right_motor, wheel_diameter = 55.5, axle_track = 125)

my_fork = Fork()
my_WH = WH()
my_move = Move()


#A villa mozgatása
fork_motor=Motor(Port.C)

#Gyro szenzor 
gs=GyroSensor(Port.S4)
gs.reset_angle(0)
#print( str(gs.angle()))

#UltrasonicSensor 
mysensor = UltrasonicSensor(Port.S3)

#print(str(mysensor.distance()))
tomb = [600,650,700,600,650,700] 
count= 0
my_move.movetoWH()
while count != 6:
    for x in range(6):
        my_move.movetocord(x,'B')
        if my_move.colorcheck(x,'B'):
            my_WH.setboxcolor(x,'W')
            break
    my_move.rollback(tomb[count])
    my_move.movetoWH()
    count += 1

count= 0
my_move.movetoWH()
while count != 6:
    for x in range(6):
        my_move.movetocord(my_WH.findbox('W'))
        if my_move.colorcheck(x,'B'):
            my_WH.setboxcolor(x,'W')
            break
    my_move.rollback(750)
    my_move.movetoWH()
    count += 1

if colorsensor.rgb()[0]<5 :
    a="black"
else :
    a="white"

def black(color):
    a == "black"

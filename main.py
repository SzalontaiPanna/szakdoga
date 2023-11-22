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

my_fork = Fork()
my_WH = WH()
my_move = Move()

"""
left_motor.run_angle(50,120)
right_motor.run_angle(50,120)
"""
robot = DriveBase(left_motor,right_motor, wheel_diameter = 55.5, axle_track = 125)

#A villa mozgatása
fork_motor=Motor(Port.C)

#Gyro szenzor 
gs=GyroSensor(Port.S4)
gs.reset_angle(0)
#print( str(gs.angle()))

#UltrasonicSensor 
mysensor = UltrasonicSensor(Port.S3)

#print(str(mysensor.distance()))

robot.straight(600)
count= 0
my_move.movetoWH()
while count != 6:
    for x in range(6):
        my_move.movetocord(x,'B')
        print("ez megvan")
        if my_move.colorcheck('B'):
            my_WH.setboxcolor(x,'W')
            break
    my_move.rollback(750)
    my_move.movetoWH()
    count += 1



"""



valami = True
while valami:
    robot.straight(10)
    print(str(mysensor.distance()))
    if mysensor.distance()<115:
        valami = False
    wait(10)








def bringbox():
    kell=['K','K']
    for x in kell:
        kordinates =my_WH.findbox(x)
        my_move.movetocord(kordinates[0],kordinates[1],kordinates[2],x)
        for y in my_WH.findbox(x):
            print("a kordináták "+str(y))


#ColorSenzor
colorsensor = ColorSensor(Port.S2)
#print(str(colorsensor.rgb()[0]))
a=""
if colorsensor.rgb()[0]<5 :
    a="black"
else :
    a="white"

def black(color):
    a == "black"

robot.straight(800)
robot.straight(-800)

while black:
    fork_motor.run_target(-700,-700)
    robot.straight(100)
    tourn(-95)
    robot.straight(750)
    ev3.speaker.beep()
    break

print(str(mysensor.distance()))

while True:
    if mysensor.distance()>70:
        fork_motor.run_target(150,150)
        robot.straight(-100)
        break
    else: 
        robot.straight(100)
        break
    
    """
"""












    

my_fork = Fork()
my_WH = WH()
my_move = Move()

def bringbox():
    kell=['K','K']
    for x in kell:
        kordinates =my_WH.findbox(x)
        my_move.movetocord(kordinates[0],kordinates[1],kordinates[2],x)
        for y in my_WH.findbox(x):
            print("a kordináták "+str(y))

def checkallbox():
    for x in range(my_WH.getlenghtofrakta()):
        for y in range(my_WH.gethightofraktar()):
            my_WH.setboxcolor(1,x,y,my_fork.getcolor())
            
 

ev3.speaker.beep()


ev3.speaker.beep(frequency=1000, duration=500)

"""
"""
#A villa mozgatása
fork_motor=Motor(Port.C)

liftdistanceCm = 1.5
degreetoCm = 0.025
levelinCm = 4.6
level = 0
islift = False 

def movetolevel(self, targetlevel):
    c = self.level - targetlevel
    self.fork.run_angle(100, ((c * self.levelinCm) / self.degreetoCm))        
    self.level = targetlevel
    print("Move to level: " + str(targetlevel))

def lift(self):
    if self.islift:
        self.fork.run_angle(100, self.liftdistanceCm / self.degreetoCm)
        self.islift = False
    else:
        self.fork.run_angle(-100, self.liftdistanceCm / self.degreetoCm)
        self.islift = True




def tourn(degree):
    robot.turn((degree-gs.angle())-15)
    for x in range(10):
        robot.turn((degree-gs.angle())/2)

boxsize=70
#A két kerék összekapcsolása
left_motor= Motor(Port.B)
right_motor= Motor(Port.A)
robot= DriveBase(left_motor,right_motor, wheel_diameter=55.5, axle_track=125)

#A villa mozgatása
fork_motor=Motor(Port.C)

#Gyro szenzor 
gs=GyroSensor(Port.S4)
gs.reset_angle(0)
print( str(gs.angle()))

#UltrasonicSensor 
mysensor = UltrasonicSensor(Port.S3)
print(str(mysensor.distance()))

#ColorSenzor
colorsensor = ColorSensor(Port.S2)
print(str(colorsensor.rgb()[0]))
a=""
if colorsensor.rgb()[0]<5 :
    a="black"
else :
    a="white"
print(a)

ev3.speaker.beep()

#Robot tevékenység 1
#Tolja le a villát, majd tegyen egy négyzetes kört majd emelje fel a villát.

fork_motor.run_target(-400,-400)
ev3.speaker.beep()
robot.straight(200)
tourn(90)
robot.straight(200)
tourn(180)
robot.straight(200)
tourn(270)
robot.straight(200)
tourn(360)
robot.straight(200)
wait(5000)
fork_motor.run_target(400,400)
ev3.speaker.beep()

#Robot tevékenység 2
#A feladat ismerje fel a fehér kockát és tegye a polcokra sorba fentről lefelé, majd a feketékkel is tegye ugyan ezt. 

if colorsensor.rgb()[0]<5 :
    a="black"

else :
    a="white"




# Write your program here.
ev3.speaker.beep()

Elindul a robot felvesz egy kockát ha fekete berakja 
a felső sorra ha fehér az alsó sorra majd visszatér a 
kockákhoz 
"""
from pybricks.ev3devices import Motor,  ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Color


class Fork:
    def __init__(self):
        self.fork = Motor(Port.C)
        self.liftdistanceCm = 1.5
        self.degreetoCm = 0.025
        self.levelinCm = 4.6
        self.level = 0
        self.islift = False
        self.colorsensor = ColorSensor(Port.S2)

    def colors(self,valami):
        a=''
        if self.colorsensor.rgb()[0]<5 :
            a="B"
        else :
            a="W"
        return a

    def colorcheck(self,color):
        if self.colors(color) == color:
            return True
        return False

    def movetolevel(self, targetlevel):
        c = self.level - targetlevel
        self.fork.run_angle(100, ((c * self.levelinCm) / self.degreetoCm))        
        self.level = targetlevel
        print("Move to level: " + str(targetlevel))

    def lift(self):
        if self.islift:
            self.fork.run_angle(100, 10)
            self.islift = False
        else:
            self.fork.run_angle(-100,10)
            self.islift = True
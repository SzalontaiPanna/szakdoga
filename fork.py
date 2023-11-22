from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.ev3devices import Motor,  ColorSensor, GyroSensor, UltrasonicSensor


class Fork:
    def __init__(self):
        self.fork = Motor(Port.C)
        self.liftdistanceCm = 1.5
        self.degreetoCm = 0.025
        self.levelinCm = 4.6
        self.level = 0
        self.islift = False 
        self.cs = ColorSensor(Port.S2)

    def colors(valami):
        szinek = {
            Color.BLACK:'B',
            Color.WHITE:'W',
        }
        return szinek.get(valami,'X')

    def colorcheck(self,color):
        if self.colors(self.cs.color) == color:
            return True
        return False

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
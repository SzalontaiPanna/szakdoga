class WH:
    def __init__(self):
        self.raktarB = ['X', 'X', 'X','X', 'X', 'X']
        self.raktarC = [['X', 'X', 'X'],['X', 'X', 'X']]
        
    def findbox(self, color):
        print("itt is voltam")
        for x in range(6):
            if self.raktarB[x] == color:
                    self.raktarB[x] = 'X'
                    return x
        #for x in range(2):
         #   for y in range(4):
          #      if self.raktarJ[x][y] == color:
           #         self.raktarJ[x][y] = 'X'
            #        return [x, y,0]

    def setboxcolor(self,x,color):
        self.raktarB[x] = colors(color)

    def colors(valami):
        szinek = {
            'W':'B',
            'B':'W',
        }
        return szinek.get(valami,'X')


    def getlenghtofraktar(self):
        return len(self.raktar[0])

    def gethightofraktar(self):
        return len(self.raktar)
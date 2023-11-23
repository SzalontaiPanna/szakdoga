class WH:
    def __init__(self):
        self.warehouse_1 = ['X', 'X', 'X','X', 'X', 'X']
        self.warehouse_2 = [['X', 'X', 'X'],['X', 'X', 'X']]
        
    def findbox(self, color):
        for x in range(6):
            if self.warehouse_1[x] == color:
                    self.warehouse_1[x] = 'X'
                    return x

    def setboxcolor(self,x,color):
        self.warehouse_1[x] = self.colors(color)

    def colors(self,valami):
        szinek = {
            'W':'B',
            'B':'W',
        }
        return szinek.get(valami,'X')


    def getlenghtofraktar(self):
        return len(self.raktar[0])

    def gethightofraktar(self):
        return len(self.raktar)
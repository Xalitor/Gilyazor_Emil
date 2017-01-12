import math
class Distance:
    #Constructor
    def __init__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0
    #Modifier
    def setValues(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0
    #Accessor
    def getMPH(self):
        return Math.sqrt((xTwo - xOne)*(xTwo-xOne)+(yTwo - yOne)*(yTwo-yOne))
    def main():
        xOne = int(input("Enter your x1 "))
        yOne = int(input("Enter your y1 "))
        xTwo = int(input("Enter your x2 "))
        yTwo = int(input("Enter your y2 "))
        #intstantiate an objects
        distance = Distance(xOne, yOne, xTwo, yTwo)
        
        

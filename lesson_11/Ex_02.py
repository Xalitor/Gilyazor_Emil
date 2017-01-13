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
    def getX1(self):
        return self.xOne
    def getY1(self):
        return self.yOne
    def getX2(self):
        return self.xTwo
    def getY2(self):
        return self.yTwo
    def getMPH(self):
        return math.sqrt((self.xTwo - self.xOne)*(self.xTwo-self.xOne)+(self.yTwo - self.yOne)*(self.yTwo-self.yOne))
    
def main():
    xOne = int(input("Enter your x1 "))
    yOne = int(input("Enter your y1 "))
    xTwo = int(input("Enter your x2 "))
    yTwo = int(input("Enter your y2 "))
    #intstantiate an objects
    distance = Distance(xOne, yOne, xTwo, yTwo)
    print("***Your inputs***")
    print("x1 ", distance.getX1())
    print("y1 ", distance.getY1())
    print("x2 ", distance.getX2())
    print("y2 ", distance.getY2())
    print("***Distance***")
    print(distance.getMPH())
main()

        

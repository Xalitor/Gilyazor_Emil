class Car:
    #Constructor
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    #Modifier
    def setCustom(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    #Accessor
    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires
def main():
    paint=input("Enter your color ")
    interior = input("Enter your interior ")
    engine = input("Enter your engine ")
    tires = input("Enter your tires ")
    #intstantiate an objects
    car1 = Car(paint, interior, engine, tires)
    print("Your vehicle is ready......")
    print("Paint:  ", car1.getPaint())
    print("Interior:  ", car1.getInterior())
    print("Engine:  ", car1.getEngine())
    print("Tires:  ", car1.getTires())
main()

class Human:
    #constructor
    def __init__(self, h, ey, s):
        self.hair = h
        self.eyes = ey
        self.skin = s
    #modifier
    def setHES(self, h, ey, s):
        self.hair = h
        self.eyes = ey
        self.skin = s
    #accessor
    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin

def main1():
    hair = input("Enter your hair's color ")
    eyes = input("Enter your eyes' color ")
    skin = input("Enter your skin's color ")
    Human1 = Human(hair, eyes, skin)
    print("Your info...")
    print("Your hair is ", Human1.getHair(),", your eyes are ", Human1.getEyes(),", your skin is ", Human1.getSkin())
main1()

class Friend:
    #Constructor
    def __init__(self, h1, ey1, s1):
        self.hair1 = h1
        self.eyes1 = ey1
        self.skin1 = s1
    #Modifier
    def setHES1(self, h1, ey1, s1):
        self.hair1 = h1
        self.eyes1 = ey1
        self.skin1 = s1
    #Accessor
    def getHair1(self):
        return self.hair1
    def getEyes1(self):
        return self.eyes1
    def getSkin1(self):
        return self.skin1
def main2():
    hair1 = input("Enter your friend's hair ")
    eyes1 = input("Enter your friend's eyes' color ")
    skin1 = input("Enter your friend's skin's color ")
    Friend1 = Friend(hair1, eyes1, skin1)
    print("Your friend's info...")
    print("Your friend's hair is ", Friend1.getHair1(),", your friend's eyes are ", Friend1.getEyes1(),", your friend's skin is ", Friend1.getSkin1())
main2()

    
    
    
    
    
        

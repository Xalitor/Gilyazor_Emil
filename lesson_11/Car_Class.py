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
    car1 = car(paint, interior, engine, tires)
    print("Your vehicle is ready......")
    print("Paint: {:<15} ", car1.getPaint())
    print("Interior: {:<15} ", car1.getInterior())
    print("Engine: {:<15} ", car1.getEngine())
    print("Tires: {:<15} ", car1.getTires())
main()
    
        

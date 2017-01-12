class MilesPerHour:
    #Constructor
    def __init__(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
    #Modifier
    def setValues(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
    #Accessor
    def GetDist(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getMPH(self):
        return self.distance/(self.hours + self.minutes/60.0)
    
        
def main():
    distance = int(input("Enter your distance "))
    hours = int(input("Enter your time (in hours)"))
    minutes = int(input("Enter your time (in minutes)"))
    #intstantiate an objects
    result = MilesPerHour(distance, hours, minutes)
    print("***Your inputs***")
    print("Distance ", result.GetDist())
    print("Time in hours ", result.getHours())
    print("Time in minutes ", result.getMins())
    print("***Result***")
    print(result.getMPH())
main()
    

    

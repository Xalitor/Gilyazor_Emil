def calcArea():
    return(3.14*(r**2))
def display():
    print("The surface area of a circle with a radius of {:.5f} is {:.5f} ".format(r, calcArea()))



r=float(input("Please, enter the radius of a circle "))


display()

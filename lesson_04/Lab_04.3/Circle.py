def setNums():
    global r
def calcArea():
    global sa
    sa = 3.14*(r**2)


r = float(input("Please, enter the radius of your circle "))

setNums()

calcArea()



print("The area of a circle with a radius of {:.5f} is {:.5f}".format(r, sa))

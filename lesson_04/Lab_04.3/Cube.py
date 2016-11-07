def setNums():
    global side
def surfaceArea():
    global sa
    sa = (side**2)*6


side = float(input("Please, enter the side of your cube "))


setNums()

surfaceArea()


print("The surface area of a cube whose sides are {:.5f} in length is {:.5f}".format(side, sa))

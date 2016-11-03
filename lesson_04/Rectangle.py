def perimeter():
    return((lenght + width)*2)
def display():
    print("Your rectangle is {:.5f} square feet".format(perimeter()))


lenght = float(input("Please, enter rectangle's leght " ))
width = float(input("Please, enter rectangle's width " ))

display()

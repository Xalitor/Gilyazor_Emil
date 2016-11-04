def setNums():
    global lenght, width
def calcPerim():
    global sum
    sum=(lenght+width)*2

lenght=float(input("Please, enter rectangle's lenght "))

width=float(input("Please, enter rectangle's width "))


setNums()

calcPerim()
print("Your rectangle is {:.5f} ft around ".format(sum))

def average():
    return((num1+num2+num3)/3)
def display():
    print("The average of {:.5f} , {:.5f} , and {:.5f} is {:.5f} ".format(num1, num2, num3, average()))


num1=float(input("Please, enter the  number 1 "))
num2=float(input("Please, enter the  number 2 "))
num3=float(input("Please, enter the  number 3 "))



display()

import math;

print("This is a program to calculate square equation for square roots.")
a = int(input("Please, enter the variable #1 "))
b = int(input("Please, enter the variable #2 "))
c = int(input("Please, enter the variable #3 "))
print("The square root #1 equal ", ((-b -math.sqrt(b**2-(4*a*c)))/2*a),".")
print("The square root #2 equal ", ((-b +math.sqrt(b**2-(4*a*c)))/2*a),".")

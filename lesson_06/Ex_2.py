number= int(input("Enter your number "))
factorial=1

for i in range(0, number):
    factorial *= (number-i)  

print(factorial)


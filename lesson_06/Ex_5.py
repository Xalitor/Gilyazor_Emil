a=int(input("Enter your first number "))
b=int(input("Enter your second number "))
output=""

for i in range(b, a+1, b):
       output=output + str(i) + " "

print(output)

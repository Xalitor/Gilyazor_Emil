numbers=[]
import random

for number in range(0, 10):
    numbers.append(random.randint(1, 100))
print("Numbers...")
output= ""
for number in numbers:
    output+=str(number) + " "
print(output)
print("________________")

def average(numbers):
    average = 0
    for number in numbers:
        average+=number
    return average/len(numbers)
print("The average of the above numbers is ", average(numbers))

number = int(input("Enter your number "))
summ=0
num=number
def sumDigits():
    global num, summ
    while num > 0:
        summ += num%10
        num = int(num/10)
sumDigits()

print("The sum of the digits in ", number," is ", summ)

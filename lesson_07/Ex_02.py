number = int(input("Enter your number "))
digits=0
average=0
summ=0
def avDigits():
    global num, digits, average, summ
    num=number
    while num > 0:
        digits += 1
        summ += num %10
        num= int(num/10)
        average = summ/ digits

avDigits()
print("The average of the digits in ", number," is ", average)
        

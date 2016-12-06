number = int(input("Enter your number "))
num=number
rev=0
def getRevers():
    global rev, num
    while num > 0:
        rev *= 10
        rev += num%10
        num=int(num/10)

getRevers()
print(number," reversed is ", rev)

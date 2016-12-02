number=int(input("Enter your number "))
size=int(input("Enter size of table "))


def graphTable():
    for i in range(1, size):
        print(i, number*i)

graphTable()

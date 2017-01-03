myList = ["pie", "computer", "human", "animal", "land"]
print("In order...")

output = ""
for i in myList:
    output += i + " "
print(output)

print("\n_____________")
print("Reversed...")


def reserve(myList):
    output = " "
    for i in range(len(myList),0,-1):
        output += myList[i-1] + " "
    print(output)

reserve(myList)



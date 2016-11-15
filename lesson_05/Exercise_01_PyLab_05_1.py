math=input("What is your Math's grade? ")
eng=input("What is your English's grade? ")
physics=input("What is your Physics's grade? ")
gym=input("What is your PE's grade? ")
art=input("What is your Sculpture's grade? ")
history=input("What is your history's grade? ")
comp=input("What is your Computer Science's grade? ")

def calcPoints():
    return((math+eng+physics+gym+art+history+comp)/7)
    if grade=="a":
        return 4.0
    if grade=="b":
        return 3.0
    if grade=="c":
        return 2.0
    if grade=="d":
        return 1.0
    if grade=="f":
        return 0.0

print("Your GPA is ", calcPoints(math) )

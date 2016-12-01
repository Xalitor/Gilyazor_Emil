global c, d
c="teacher"
d="computer"


def passCheck():
    a=input("Enter your username... ")
    b=input("Enter your password... ")
    if c==a and d==b:
        print("You are granted access!")
    elif c==a:
        print("Your password is incorrect!")
    elif d==b:
        print("Your username is incorrect!")
    else:
        print("Your username and password are incorrect!")


passCheck()
    

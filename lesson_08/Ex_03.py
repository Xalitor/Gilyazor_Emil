number = int(input("Enter your number "))
def luck(number):
    if number > 0:
        if  number %10 == 7:
            return 1+luck(int(number/10))
        else:
            return 0 + luck(int(number/10))
    else:
        return 0


print(luck(number))
        
            
          

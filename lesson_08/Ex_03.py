number = int(input("Enter your number "))
def luck(number):
    if number > 0:
        if  number %10 == 7:
            return (number %10)+1
        else:
            return (number%10) + 0
    else:
        return 0


print(luck(number))
        
            
          

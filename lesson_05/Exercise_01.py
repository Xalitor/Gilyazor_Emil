import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)



def rollDice():
    if num1==num2:
        print("The winner is no one")
    if num1 <= num2:
        print("You win!")
    if num2 <= num1:
        print("Computer wins!")

print("You rolled a ", num2,".")
print("Computer rolled a ", num1,".")


rollDice()


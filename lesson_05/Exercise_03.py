global height, weght, bmi
bmi=0


height=float(input("What is your height in inches?"))
weight=float(input("What is your weight in pounds?"))


bmi=(weight/(height*height))*703

def calcBMI(bmi):
    if bmi<18.5:
        print(" Condition is Underweight.")
    elif bmi>=18.5 and bmi<=24.9:
        print("Condition is  Normal.")
    elif bmi>=25 and bmi<=29.9:
        print("Condition is Overweight")
    elif bmi>=30 and bmi<=34.9:
        print("Condition is Obese")
    elif bmi>=35 and bmi<=39.9:
        print("Condition is Very Obese")
    elif bmi>=40:
        print("Condition is Morbidly Obese")



calcBMI(bmi)

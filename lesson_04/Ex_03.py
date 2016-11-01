def format (P, r, n, t):
    return((P*((1+(r/n))**(n*t)))/(t*12))
P = float(input("Please, enter principal number "))
r = float(input("Please, enter interest rate "))
n = float(input("Please, enter number of times the loan is compounded per year "))
t = float(input("Please, enter life of the loan (in years) "))
print("Your total cost of the loan is",((P*((1+(r/n))**(n*t)))/(t*12)) , ".")

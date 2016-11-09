global discount, subtotal, total
dicount=0
subtotal=0
total=0
item1 = input("Please, enter first item ")
price1 = float(input("Please, enter first price "))
item2 = input("Please, enter second item ")
price2 = float(input("Please, enter second price "))
item3 = input("Please, enter third item ")
price3 = float(input("Please, enter third price "))
item4 = input("Please, enter fourth item ")
price4 = float(input("Please, enter fourth price "))




subtotal = price1+price2+price3+price4

tax = subtotal*0.08

def discount():
    if subtotal>=2000:
        discount=subtotal*0.15
    if subtotal<=2000:
        discount=subtotal*0
discount()

total = subtotal - discount + tax


print("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
print("{:.2f} = , {:.2f} = {:.2f}, {:.2f} = {:.2f}, {:.2f} = {:.2f}".format(item1, price1, item2, price2, item3, price3, item4, price4))
print("Subtotal is {:.2f}".format(subtotal))
print("Discount is {:.2f}".format(discount))
print("____________________________________")
print("Total is {:.2f}".format(total))
print("Thank you!")

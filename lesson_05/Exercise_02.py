global discount, subtotal, total
subtotal=0;
discount=0;
total=0;
def format (item, price):
    print("{:<15}.........${:10.2f}".format(item, price))

def discount():
    global subtotal, discount, total
    if subtotal >= 2000:
        discount=subtotal * 0.15
    if subtotal <= 2000:
        discount=0



item1 = input("Please, enter first item ")
price1 = float(input("Please, enter first price "))
item2 = input("Please, enter second item ")
price2 = float(input("Please, enter second price "))
item3 = input("Please, enter third item ")
price3 = float(input("Please, enter third price "))
item4 = input("Please, enter fourth item ")
price4 = float(input("Please, enter fourth price "))

subtotal = price1+price2+price3+price4
discount()
tax = subtotal*0.08
total = subtotal-discount+tax

print("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)

format("Subtotal", subtotal)
format("Discount", discount)
format("Total", total)
print("_______________________________")
print("Thank you!")

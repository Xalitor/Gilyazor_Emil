def format(item, price):
    print("*  {:<16}........      {:<10.2f}".format(item, price))
item1 = input("Please enter item 1 ")
price1 = float(input("Please enter price "))

item2 = input("Please enter item 2 ")
price2 = float(input("Please enter price "))

item3 = input("Please enter item 3 ")
price3 = float(input("Please enter price "))

subtotal = price1+price2+price3
tax = 0.075
tax1 = subtotal*tax

print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)

format("Subtotal", subtotal)
format("Tax", tax1)
format("Total", subtotal+tax1)
print("__________________________________________")
print("* Thanks you for your support *")

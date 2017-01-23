import random
class Item:
    #Constructor
    def __init__(self, man, n, cat = "", pr = ""):
        self.manufacturer = man
        self.name = n
        self.category = cat
        self.UPC = random.randint(1000000000, 9999999999)
        self.price = pr
    #Modifier
    def setValues(self, man, n, cat, UPC, pr):
        self.manufacturer = man
        self.name = n
        self.category = cat
        self.UPC = gr
        self.price = pr
    #Accessor
    def getMan(self):
        return self.manufacturer
    def getN(self):
        return self.name
    def getCat(self):
        return self.category
    def getPr(self):
        return self.price
    def getGr(self):
        return self.UPC
    def __str__(self):
        return "Item's Info...\nManufacturer: " + self.manufacturer + \
                              "\nName: " + self.name + \
                              "\nCategory: " + self.category + \
                              "\nPrice: " + self.price + \
                              "\nUPC: " + str(self.UPC)
                            
            


def main():
    
    manufacturer = input("Enter item's manufacure ")
    name = input("Enter item's name ")
    dop = input("Do you want to print category and price? y or n? ")
    if dop == "n":
        item1 = Item(manufacturer, name)
    else:
        category = input("Enter item's category ")
        price = input("Enter item's price ")
        item1 = Item(manufacturer, name, category, price)
    print(item1)
main()
            
            
    

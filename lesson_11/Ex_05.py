import random
class User:
    #constructor
    def __init__(self, fName, lName, a = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = a
        self.userID = random.randint(0, 100000000)
    #modifier
    def setValue(self, fName, lName, a, ID):
        self.firstName = fName
        self.lastName = lName
        self.avatar = a
        self.userID = random.randint(0, 100000000)
    #Accessor
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getAvatar(self):
        return self.avatar
    
    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                               "\nLast Name: " + self.lastName + \
                               "\nAvatar: " + self.avatar + \
                               "\nUser ID#: " + str(self.userID)
def main():
    firstName = input("Enter your first name ")
    lastName = input("Enter your last name ")
    avatar1 = input("Would you like to use a public avatar? n or y? ")
    if avatar1 == "n":
        user1 = User(firstName, lastName)
    else:
        avatar = input("Enter your avatar ")
        user1 = User(firstName, lastName, avatar1)
    print(user1)
main()

            

            





    
    
    
    

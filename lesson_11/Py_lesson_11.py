class UserNames:
    #Constructor
    def __init__(self, fName, lName, uName):
        self.firstName = fName
        self.lastName = lName
        self.userName = uName
    #Modifier
    def setUserName(self, newUser):
        self.userName = newUser

    
    #Accessor
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getUserName(self):
        return self.userName
def main():
    firstName = input("Enter your first name ")
    lastName = input("Enter yuor last name ")
    userName = input("Enter your desired user name ")

    #instantiate an objects
    user1 = UserNames(firstName, lastName, userName)
    print("<<<<<<<<USER INFO>>>>>>>>>>>>>")
    print("Name: ", user1.getFirstName()," ", user1.getLastName())
    print("User Name ", user1.getUserName(),"\n\n")

    user1.setUserName("Xalitor")

    print("<<<<<<<<USER INFO>>>>>>>>>>>>>")
    print("Name: ", user1.getFirstName()," ", user1.getLastName())
    print("User Name ", user1.getUserName(),"\n\n")


main()
    

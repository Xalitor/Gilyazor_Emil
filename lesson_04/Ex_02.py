def format(name, second):
    print("* {:>10}         {:<10} *".format(name, second))
name1 = input("Enter your first name: ")
second1 = input("Enter your last name: ")

name2 = input("Enter your your title: ")
second2 = input("Enter the school site: ")

name3 = input("Enter the school year: ")
second3 = input("What is your subject: ")

print("***********************************")
format(second2, name3)
format(name1, second1)
format(name2, second3)
print("***********************************")


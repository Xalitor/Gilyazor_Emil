word1 = input("Enter your first word ")
word2 = input("Enter your second word ")
word3 = input("Enter your third word ")

def makeCenter(word):
    if len(word)>=20:
        return word
    else:
      return " " + word + " "

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
    

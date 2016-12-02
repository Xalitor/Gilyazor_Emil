word=input("Enter your word ")

def keepStay():
    for i in range(0, len(word), 1):
        print(word[i:len(word)])


keepStay()

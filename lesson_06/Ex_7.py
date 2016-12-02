word=input("Enter your word ")

def keepStay():
    for i in range(len(word), 0,  -1):
        print(word[i:len(word)])


keepStay()

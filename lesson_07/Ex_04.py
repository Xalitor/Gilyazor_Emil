sentence = input("Enter your sentence ")

top=0;


def replace():
    global sentence, top
    while top < sentence.count("a") > 0:
        sentence = sentence[0: sentence.index("a")] + "@" + sentence[sentence.index("a")+1 : len(sentence)]

replace()

print(sentence)


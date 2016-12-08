sentence = input("Enter your sentence ")

def repLace(sentence):
    if (" " not in sentence):
        return sentence
    else:
        return sentence[0: sentence.index(" ")] +"_"+ repLace(sentence[sentence.index(" ")+1 : len(sentence)])

print(repLace(sentence))
        
    

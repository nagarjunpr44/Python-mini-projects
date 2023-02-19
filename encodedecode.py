from random import choices
from string import ascii_lowercase

answer=input("Do you want to encode or decode(encode/decode)\n").lower()

if answer=="encode":
    word=input("Enter the word you want to encode\n")
    words=word.split(" ")
    nwords=[]
    for wordss in words:
        if (len(wordss)>=3):
            r1=["".join(choices(ascii_lowercase,k=3))for _ in range(2)]
            #print(type(r1))
            new_word=r1[0]+wordss[1:]+wordss[0]+r1[1]
            nwords.append(new_word)
            
        else:
            nwords.append(wordss[::-1]) 
    print(" ".join(nwords))        

elif answer=="decode":
    word=input("Enter the word you want to decode\n")
    words=word.split(" ")
    nwords=[]
    for wordss in words:
        if len(wordss)<3:
            nwords.append(wordss[::-1]) 
        else:
            word=wordss[3:-3]
            word=word[-1]+word[:-1]
            nwords.append(word)        
    print(" ".join(nwords))     
else:
    print("Invalid input")





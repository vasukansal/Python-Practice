#ENCODING RULES --
#if name contains 3 or more characters then revrse the name and add 3 random characters before and after the name
#if name contains less than 3 characters then only reverse it

#Question Given by - https://www.youtube.com/watch?v=pOWJ6WgVRIU&t=246s

import random
def Encoding(name):
    name2=""
    if len(name)>=3:
        for i in range(0,len(name)):
            if i!=0:
                name2=name2+name[i]
        name2=name2+name[0]
        list1=[]
        enco1=""
        while(len(list1)!=3):
            list1.append(random.randrange(65,91))
        for i in list1:
            enco1=enco1+chr(i)
        name2=enco1+name2
        list1.clear()
        while(len(list1)!=3):
            list1.append(random.randrange(97,123))
        enco1=""
        for i in list1:
            enco1=enco1+chr(i)
        name2=name2+enco1
        return(name2)
    if len(name)<3:
        return(name[::-1])

def Decoding(NAME):
    if (len(NAME)<3):
        return(NAME[::-1])
    if len(NAME)>=3:
        lent=len(NAME)
        count=0
        name2=""
        name2=NAME[3:(lent-3)]
        lent2=len(name2)
        name3=name2[lent2-1]+name2[0:(lent2)-1]
        return(name3)
print("Enter your name - ")
enc=Encoding(input())
print("Encoded text - ",enc)
dec=Decoding(enc)
print("Decoded text - ",dec)

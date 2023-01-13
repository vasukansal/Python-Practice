#Tried to make mini KBC game ;)

quest=["Q1. What is your name?","Q2. What is your surname?","Q3. What is your gender?", "Q4. Which language is this?","Q5. Is this code running properly?"]
answer=["Vasu","Kansal","Male","Python","Yes"]
options=[["Yami","VK","Vasu","Kami"],["Kami","Kansal","K","KK"],["Male","Female","Other","PNS"],["C","Python","Java","C++"],["Yes","Maybe","No","Partially"]] #PNS - Prefer not to say

while(1>0):
    money=0
    k=0
    print("\n->Enter '1' to play \n->Enter '2' to exit1")
    choice=int(input())
    if(choice==1):
        for i in quest:
            print(i)
            print(options[k])
            a=input()
            for j in answer:
                if(a==j):
                    money=money+(1000*(k+1))
            k=k+1
        print("\nMoney won -- ")
        print(money)
    elif(choice==2):
        print("BYEE :)")
        break

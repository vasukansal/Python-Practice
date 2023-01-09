import time
hours=int(time.strftime("%H"))
minute=int(time.strftime("%M"))
seconds=int(time.strftime("%S"))
# print(hours+" "+minute+" "+seconds)
if(4<=hours<=11 and minute<=59 and seconds<=59):
    print("Good Morning!! :)")

elif(12<=hours<=16 and minute<=59 and seconds<=59):
    print("Good Afternoon!! :)")

elif(17<=hours<=21 and minute<=59 and seconds<=59):
    print("Good Evening!! :)")

elif(22<=hours<=23 or 0<=hours<=3 and minute<=59 and seconds<=59):
    print("Good Noght!! :)")

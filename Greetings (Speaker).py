import pyttsx3
import time
hours=int(time.strftime("%H"))
minute=int(time.strftime("%M"))
seconds=int(time.strftime("%S"))
engine = pyttsx3.init()
Gender=engine.getProperty("voices")
engine.setProperty('rate',150)
engine.setProperty("voice",Gender[1].id)
if(4<=hours<=11 and minute<=59 and seconds<=59):
    engine.say("Good Morning Vaasu")

elif(12<=hours<=16 and minute<=59 and seconds<=59):
    engine.say("Good Afternoon Vaasu")

elif(17<=hours<=21 and minute<=59 and seconds<=59):
    engine.say("Good Evening Vaasu")

elif(22<=hours<=23 or 0<=hours<=3 and minute<=59 and seconds<=59):
    engine.say("Good Night Vaasu")


engine.runAndWait()
engine.stop()
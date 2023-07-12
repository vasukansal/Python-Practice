from plyer import notification
import pyttsx3
import time
tile="Drink Water"
Nmess="30 min. has passed since you last drank"
engine = pyttsx3.init()
Gender=engine.getProperty("voices")
engine.setProperty('rate',115)
engine.setProperty("voice",Gender[0].id)
i=0
while( i in range(0,5)):
        notification.notify(        
                title=tile,
                message=Nmess,
                app_icon="drink_119593.ico",
                timeout=5,
                toast=False) 
        engine.say("Drink water")
        engine.runAndWait()
        engine.stop()
        # time.sleep(60*30)
        i=i+1  
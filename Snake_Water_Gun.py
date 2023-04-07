import random
import time
while(1>0):
    list=[0,1,2]
    computer=random.choice(list)
    print("\nWelcome to Snake Water Gun, Enter  - ")
    print("0 for Snake")
    print("1 for Water")
    print("2 for Gun")
    print("3 to exit the game\n")
    player=int(input("Input - "))
    if player==3:
        print("Bye Bye")
        break
    print(f"\nYou chose {player}")
    time.sleep(0.3)
    print(f"Opponent chose {computer}")
    time.sleep(0.8)
    if computer==player:
        print("\n!!!! Result - Draw !!!!")
    elif computer==(player+1) or computer==(player-2):
        print("\n!!!! Result - WON :) !!!!")
    else:
        print("\n!!!! Result - You Lose :( !!!!") 
    time.sleep(1.3)
#TASK 4 ROCK,PAPER,SCISSOR GAME

import random

computer=random.choice([1,0,-1])
yourchoice=(input("enter your choice:"))
yourdict={"r":1,"p":-1,"s":0}
revrersedict={1:"rock",-1:"paper",0:"scissor"}
you=yourdict[yourchoice]
print(f"your choice :{revrersedict[you]}\ncomputer choice :{revrersedict[computer]}")

if(computer==you):
    print("it's an draw")
else:
    if(computer==1 and you==-1):
        print("you wins!")
    elif(computer==1 and you==0):
        print("computer wins!")
    elif(computer==-1 and you==1):
        print("computer wins!")
    elif(computer==-1 and you==0):
        print("you win!!")
    elif(computer==0 and you==1):
        print("you win!")
    elif(computer==0 and you==-1):
        print("computer wins!")
    else:
        print("something went wrong")

print("'wanna try again'")
        
        

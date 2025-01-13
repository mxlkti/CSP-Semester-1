#Titus Lau
#Period 5
#01/07/25

#init
import random

#functions
def game():
    win=0
    lose=0
    tie=0

    print('\033[1m'+"Welcome to Rock, Paper, Scissors!"+'\033[0m')
    print(" ")
    tut=input("Would you like a tutorial on how to play?")
    tut=tut.lower()
    if tut=="yes" or tut=="y":
        print("Rock, Paper, Scissors is a hand game played where")
        print("Rock beats scissors,")
        print("scissors beats paper,")
        print("and paper beats rock.")
        print(" ")
    elif tut=="no" or tut=="n":
        print("Let's get started!")

    while True:
        print("Make your move!")
        sign=input("Please choose rock, paper, or scissors.")
        sign=sign.lower()
        if sign=="rock" or sign=="r":
            sign=1
        elif sign=="paper" or sign=="p":
            sign=2
        elif sign=="scissors" or sign=="s":
            sign=3

        if sign==1:
            print("You have selected rock.")
        elif sign==2:
            print("You have selected paper.")
        elif sign==3:
            print("You have selected scissors.")
        print(" ")

        comp=random.randint(1,3)
        if comp==1:
            print("The computer has selected rock.")
        if comp==2:
            print("The computer has selected paper.")
        if comp==3:
            print("The computer has selected scissors.")

        if sign==comp:
            print("TIE!")
            tie=tie+1
        elif sign==1 and comp==2:
            print("PLAYER LOST!")
            lose=lose+1
        elif sign==1 and comp==3:
            print("PLAYER WIN!")
            win=win+1
        elif sign==2 and comp==1:
            print("PLAYER WIN!")
            win=win+1
        elif sign==2 and comp==3:
            print("PLAYER LOST!")
            win=win+0
            lose=lose+1
        elif sign==3 and comp==1:
            print("PLAYER LOST!")
            lose=lose+1
        elif sign==3 and comp==2:
            print("PLAYER WIN!")
            win=win+1
        print(" ")
        print("Score is: "+str(win)+"-"+str(lose))
        print("You have "+tie+" ties.")

        again=input("Would you like to play another round?")
        again=again.lower()
        if again=="no" or again=="n":
            print("Thank you for playing!")
            break
        if again=="yes" or again=="y":
            print("Game restarting...")
            print(" ")

#main
game()

#Multiplication Quiz

#init
import random
import time
import math
correct=0 #question counter
count=0 #endless question counter
#functions
def quiz():
    global correct
    global count

    print("Welcome to the Multiplication Quiz")
    print("Try to answer these questions as fast as you can!")
    print(" ")
    end=input("Would you like to try endless mode?")
    end=end.lower()

    if end=="yes" or end=="y": #endless mode
        print("To stop at any time, please enter 'stop'")
        correct=0
        start_time=time.time() #start timer
        while True:
            num1=random.randint(1,12)
            num2=random.randint(1,12)
            question_end=input("What is "+str(num1)+" x "+str(num2)+"?")
            if question_end.lower()=="stop":
                end_time=time.time() #end time
                stopwatch=math.floor(end_time-start_time)
                print(" ")
                print("You got "+str(correct)+"/"+str(count)+" questions correct!")
                print("You answered "+str(count)+" questions in "+str(stopwatch)+" seconds!")
                print("Thank you for playing!")
                break
            print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
            print("Your answer was "+str(question_end))
            if int(question_end)==int(num1*num2):
                correct=correct+1
                print("Correct!")
                print(" ")
            else:
                print("Incorrect!")
                print(" ")
            count=count+1

    elif end=="no" or end=="n": #level directory
        while True: #number of questions
            num=input("How many questions do you want to answer? Choose a number between 3-10.")
            if 3<=int(num)<=10:
                print("Thank you, let's get started.")
                print(" ")

            level=input("Please select a level: easy, medium, or hard")
            level=level.lower()

            start_time=time.time() #start timer

            if level=="easy" or level=="e":
                for i in range(int(num)):
                    num1=random.randint(1,4)
                    num2=random.randint(1,4)
                    question_e=input("What is "+str(num1)+" x "+str(num2)+"?")
                    print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
                    print("Your answer was "+str(question_e))
                    if int(question_e)==int(num1*num2):
                        correct=correct+1
                        print("Correct!")
                        print(" ")
                    else:
                        print("Incorrect!")
                        print(" ")

            elif level=="medium" or level=="med" or level=="m":
                for i in range(int(num)):
                    num1=random.randint(4,7)
                    num2=random.randint(4,7)
                    question_m=input("What is "+str(num1)+" x "+str(num2)+"?")
                    print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
                    print("Your answer was "+str(question_m))
                    if int(question_m)==int(num1*num2):
                        correct=correct+1
                        print("Correct!")
                        print(" ")
                    else:
                        print("Incorrect!")
                        print(" ")

            elif level=="hard" or level=="h":
                for i in range(int(num)):
                    num1=random.randint(6,12)
                    num2=random.randint(6,12)
                    question_h=input("What is "+str(num1)+" x "+str(num2)+"?")
                    print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
                    print("Your answer was "+str(question_h))
                    if int(question_h)==int(num1*num2):
                        correct=correct+1
                        print("Correct!")
                        print(" ")
                    else:
                        print("Incorrect!")
                        print(" ")

            end_time=time.time() #end time
            stopwatch=math.floor(end_time-start_time)
            print(" ")
            print("You got "+str(correct)+"/"+str(num)+" questions correct!")
            print("You answered "+str(num)+" questions in "+str(stopwatch)+" seconds!")

            again=input("Would you like to play again?")
            again=again.lower()
            if again=="yes" or again=="y":
                correct=0
                print("Game restarting...")
                print(" ")
            elif again=="no" or again=="n":
                print("Thank you for playing!")
                break

#main
quiz()

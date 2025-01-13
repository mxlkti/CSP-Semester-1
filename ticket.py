#Ticket Generator

#init
import turtle
t=turtle.Turtle()

#function    
def ticket_quiz():
    
    def draw_ticket(name, price, dayofweek, y_location):
        t.goto(-50, y_location)
        t.write("Ticket", font=("Arial", 15), align="right")
        t.pendown()
        for i in range(2):
            t.forward(500)
            t.left(90)
            t.forward(250)
            t.left(90)
        t.penup()
        t.goto(50, y_location +215)
        t.write("Admit One", font=("Arial", 15), align="right")
        t.goto(440, y_location +215)
        t.write(dayofweek, font=("Arial", 15), align="right")
        t.goto(200, y_location +115)
        t.write(name, font=("Arial", 20), align="center")
        t.goto(200, y_location +15)
        t.write("$"+str(price), font=("Arial", 15), align="center")
    
    print("Welcome to the Museum of Titus!")
    print("We heard you were interested in a visit.")
    print("We need to ask you some questions before buying a ticket.")
    print(" ")
    first=input("What is your first name? ")
    last=input("What is your last name? ")
    name=first+" "+last
    print("Thank you, "+first+"!")
    while True:
        age=int(input("What is your age? "))
        if age<=0:
            print("I don't think sperm cells can see, try putting in your real age.")
        elif age>=115:
            print("Wow you're really old, try putting in your real age.")
        else:
            break
    if age<=3:
        age="3 and under"
    elif age<=17:
        age="Kid"
    else:
        age="Adult"
    while True:
        if age=="Kid" or age=="Adult":
            student=input("Are you a high school, or college student? ")
            if student=="yes" or student=="Yes" or student=="YES" or student=="y" or student=="Y":
                age=="Kid"
                student="yes"
                print("You qualify for the student discount!")
                break
            elif student=="no" or student=="No" or student=="NO" or student=="n" or student=="N":
                student="no"
                break
            else:
                print("I didn't get that, please try typing 'yes' or 'no'.")
    while True:
        day=input("What day do you plan to visit the museum? ")
        if day=="sunday" or day=="su" or day=="Sunday" or day=="sun":
            day="Sunday"
            break
        elif day=="monday" or day=="mo" or day=="Monday" or day=="mon":
            day="Monday"
            break
        elif day=="tuesday" or day=="tu" or day=="Tuesday" or day=="tue" or day=="tues":
            day="Tuesday"
            break
        elif day=="wednesday" or day=="we" or day=="Wednesday" or day=="wed":
            day="Wednesday"
            break
        elif day=="thursday" or day=="th" or day=="Thursday" or day=="thu" or day=="thurs":
            day="Thursday"
            break
        elif day=="friday" or day=="fr" or day=="Friday" or day=="fri":
            day="Friday"
            break
        elif day=="saturday" or day=="sa" or day=="Saturday" or day=="sat":
            day="Saturday"
            break
        else:
            print("I didn't get that, try typing 'Monday' or 'Friday'.")
    print(" ")
    print("We are getting ready for your visit on "+day+".")
    coupon=input("Do you have a coupon code for your visit? ")
    if coupon=="FREEFRIDAY" and age=="Adult" and student=="no":
        print("I'm sorry, that coupon is only valid or children and students.")
    elif coupon=="FREEFRIDAY" and age=="Kid" and day=="Friday":
        print("Coupon FREEFRIDAY succesful! You are eligible for a free visit.")
        coupon=1
    elif coupon=="FREEFRIDAY" and age=="Kid" and day!="Friday":
        print("I'm sorry, that coupon is only valid on Fridays.")
        
    elif coupon=="SUNDAY10" and age=="Adult" and student=="no":
        print("I'm sorry, that coupon is only valid or children and students.")
    elif coupon=="SUNDAY10" and age=="Kid" and day=="Sunday":
        print("Coupon SUNDAY10 succesful! You are eligible for $10 off.")
        coupon=2
    elif coupon=="SUNDAY10" and age=="Kid" and day!="Sunday":
        print("I'm sorry, that coupon is only valid on Sunday.")
    else:
        print("Coupon code invalid.")
        
    if age=="Kid" and student=="yes":
        age="Student"

    print(" ")
    print(name+", you are eligible for a "+age+" Ticket on "+day+".")
    if age=="3 and under":
        price=0
    elif age=="Kid" or age=="Student":
        price=50
        if day=="Saturday" or day=="Sunday":
            price=100
        if coupon==1:
            price=0
        elif coupon==2:
            price=price-10
    elif age=="Adult":
        price=100
    print("Your total is $"+str(price)+".")
    print("Please proceed to the payment screen to pay and claim your ticket.")
    draw_ticket(name, price, day, 0)
    
#main
#draw_ticket("Titus Lau", 5, "Friday", 0)
ticket_quiz()

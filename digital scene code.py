#Snoopy Drawing

#init
import turtle
turtle=turtle.Turtle()

#function
    
def snoopy(size,pos_x,pos_y):
    
    def origin(): #goes to starting point
        turtle.penup()
        turtle.goto(pos_x,pos_y)
        turtle.pendown()
        turtle.seth(0)

    def ear_start(): #draws a section of the ear and upper head
        origin()
        turtle.seth(60)
        turtle.circle(size*0.5,60)
        turtle.circle(size*-0.7,70)
        turtle.circle(size*-1.2,70)
        turtle.circle(size*-0.15,30)
        turtle.circle(size*0.6,50)
        turtle.right(15)
        turtle.circle(size*-1.8,70)

    def snout_start(): #draws a section of the snout
        origin()
        turtle.seth(240)
        turtle.circle(size*-0.6,30)
        turtle.circle(size*1.2,40)

    def arm(): #draws the arm
        turtle.circle(size*-2,25)
        turtle.seth(0)
        turtle.fd(size*3.05)

    def snoopy_color(): #fills in the character white
        turtle.color("white")
        origin()
        turtle.begin_fill()
        ear_start()
        turtle.circle(size*-0.4,100)
        turtle.circle(size*-1.8,70)

        snout_start()
        turtle.end_fill()
        turtle.begin_fill()
        turtle.circle(size*0.9,70)
        turtle.circle(size*0.7,80)
        turtle.circle(size*-2.5,20)
        arm()

        turtle.width(3)
        ear_start()
        turtle.seth(0)
        turtle.circle(size*0.6,80)
        turtle.circle(size*-0.9,70)
        turtle.fd(size*0.5)
        turtle.seth(-90)
        turtle.fd(size*2.45)
        turtle.end_fill()

        turtle.begin_fill()
        turtle.seth(160)
        turtle.fd(size*5)
        snout_start()
        turtle.circle(size*0.9,70)
        turtle.circle(size*0.7,80)
        turtle.circle(size*-2.5,20)
        arm()
        turtle.end_fill()
    
    turtle.speed(12) #lineart starts here
    turtle.width(3)
    snoopy_color()
    turtle.color("black")
    ear_start()
    turtle.circle(size*-0.4,100)
    turtle.circle(size*-1.8,70)

    turtle.penup() #black ear fill in
    turtle.seth(0)
    turtle.fd(size*0.2)
    turtle.left(90)
    turtle.fd(size*0.08)
    turtle.seth(95)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.circle(size*-0.4,100)
        turtle.circle(size*-1.3,80)
    turtle.end_fill()

    snout_start()
    turtle.circle(size*0.9,70)
    turtle.circle(size*0.7,80)
    turtle.circle(size*-2.5,20)
    
    origin()
    turtle.penup()
    turtle.fd(size*0.5)
    turtle.right(90)
    turtle.fd(size*0.2)
    turtle.pendown()
    turtle.begin_fill() #draws the eye
    turtle.seth(-20)
    for i in range(2):
        turtle.circle(size*0.05,90)
        turtle.circle(size*0.2,90)
    turtle.end_fill()

    snout_start()
    turtle.circle(size*0.9,50)
    turtle.seth(0)
    turtle.fd(size*0.05)
    turtle.seth(110)
    turtle.begin_fill()
    turtle.circle(size*0.12) #draws the nose
    turtle.end_fill()

    snout_start()
    turtle.circle(size*0.9,70)
    turtle.circle(size*0.7,80)
    turtle.circle(size*-2.5,20)
    arm()

    ear_start() #collar
    turtle.circle(size*-0.4,100)
    turtle.circle(size*-1.8,10)
    turtle.seth(-90)
    turtle.width(size*0.12)
    turtle.fd(size*0.75)

    turtle.width(3) #draws the back
    ear_start()
    turtle.seth(0)
    turtle.circle(size*0.6,80)
    turtle.circle(size*-0.9,70)
    turtle.fd(size*0.5)
    
#main
snoopy(120,-200,70)

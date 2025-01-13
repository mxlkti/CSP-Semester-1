#Jigglypuff Line Drawing

#initliaize
import turtle
ava = turtle.Turtle()
titus = turtle.Turtle()

#function
#these two functions place the pen up/down because we are lazy
def up():
    titus.penup()
def down():
    titus.pendown()
    ava.pendown()
#this function outlines the outside of titusglypuff's body, and it's broken
#into segments so things like ears and feet can be drawn

def bottomBody(): #outlines the circular bottom of the titusglypuff
    ava.penup()
    ava.goto(-200,-200)
    ava.down()

    ava.seth(-45)
    ava.circle(220, 80)
    ava.circle(240,80)
    ava.penup()
    ava.circle(220, 45)
    down()

    ava.circle(220, 20)
    ava.penup()
    ava.circle(220,70)
    down()
    ava.circle(240,45)
    ava.seth(-150)

def arm1():#Draws the arm on the left side of the drawing
    ava.circle(95, 60)
    ava.circle(10,70)
    ava.circle(72, 80)

    ava.seth(-270)
    ava.circle(80,29)

    ava.penup()
    ava.goto(-200,-200)
    
def ear2(): #draws the outline of the ear on the right
    ava.seth(-45)
    ava.down()

    ava.circle(220, 80)
    ava.circle(240,80)
    
    ava.seth(49)
    ava.circle(220, 40)
    ava.seth(171)
    ava.circle(300,35)
    ava.penup()

def ear1(): #outlines the first ear, which is on the left
    ava.goto(-138,200)
    ava.down()
    ava.seth(150)
    ava.circle(180,55)
    ava.seth(-85)
    ava.circle(275, 34)

def innerEar1():#this makes the inner, shaded region of the first ear (on the left)
    ava.penup()
    ava.goto(-284,195)
    down()
    ava.seth(-80)
    ava.begin_fill()
    ava.circle(200,35)

    ava.seth(53)
    ava.forward(100)
    
    ava.seth(150)
    ava.circle(200,34)
    down()
    ava.end_fill()

def innerEar2(): #this makes the inner, shaded region of the second ear (on the right)
    ava.penup()
    ava.goto(131,88)
    down()
    ava.begin_fill()
    ava.seth(42)
    ava.circle(250,30)

    ava.seth(170)
    ava.circle(200,45)

    ava.seth(-45)
    ava.forward(110)
    ava.end_fill()

def arm2(): #draws the arm on the right, inside the titusglypuff
    ava.penup()
    ava.goto(20,-120)
    down()
    ava.seth(20)
    ava.circle(-120,12)

    ava.seth(-35)
    ava.circle(-95, 40)
    ava.circle(-20,70)
    ava.circle(-42, 100)
    ava.penup()
    ava.goto(180,180)
    
def wig(): #makes the curly lump thing
    titus.penup()
    titus.goto(-22,150)
    titus.pendown()

    titus.seth(90)
    titus.circle(80,40)
    
    titus.seth(135)
    titus.circle(65,90)
    titus.circle(135,90)
    titus.circle(40,90)
    titus.circle(75,60)

    titus.seth(-110)
    titus.circle(-40,80)
    
def eye1(): #makes left eye
    up()
    titus.goto(-210,-70)
    down()
    titus.seth(-45)
    titus.begin_fill()
    for i in range(2):
        titus.circle(24,90)
        titus.circle(56,90)
    titus.end_fill()
        
    titus.seth(225)
    up()
    titus.fd(20)
    down()
    titus.seth(-45)
    for i in range(2):
        titus.circle(40,90)
        titus.circle(72,90)
        
    up()
    titus.goto(-210,-10)
    down()
    titus.begin_fill()
    titus.circle(12)
    titus.color("white")
    titus.end_fill()
    titus.color("black")

def eye2(): #makes right eye
    up()
    titus.goto(-25,-65)
    down()
    titus.seth(-45)
    titus.begin_fill()
    for i in range(2):
        titus.circle(40,90)
        titus.circle(48,90)
    titus.end_fill()
        
    titus.seth(225)
    up()
    titus.fd(20)
    down()
    titus.seth(-45)
    for i in range(2):
        titus.circle(56,90)
        titus.circle(64,90)
        
    up()
    titus.goto(-10,-10)
    down()
    titus.begin_fill()
    titus.circle(12)
    titus.color("white")
    titus.end_fill()
    titus.color("black")

def smile(): #makes mouth
    up()
    titus.goto(-130,-100)
    down()
    titus.seth(-45)
    titus.circle(40,90)

def foot1(): #makes the left foot
    up()
    titus.goto(-50,-265)
    titus.seth(-90)
    down()
    titus.fd(15)
    titus.seth(200)
    titus.circle(-500,17)
    titus.circle(-25,170)
    titus.seth(30)
    titus.circle(-160,22)

def foot2(): #makes the right foot
    up()
    titus.goto(76,-230)
    titus.seth(0)
    down()
    titus.circle(-45,80)
    titus.circle(-20,20)
    titus.seth(220)
    titus.circle(-110,50)
    titus.circle(-40,40)
    titus.seth(110)
    titus.circle(-90,17)

def jigglypuff(): #makes the drawing
    ava.speed(10)
    titus.speed(10)
    ava.width(2.5)
    titus.width(2.5)
    bottomBody()
    arm1()
    ear2()
    ear1()
    innerEar1()
    innerEar2()
    arm2()
    wig()
    eye1()
    eye2()
    smile()
    foot1()
    foot2()
    up()
    titus.goto(140,120)

#main
jigglypuff()

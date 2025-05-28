#init
from tkinter import *
import random

root = Tk() #creates the main window
root.title("Pixel Picture")
root.geometry("1200x1200")

#all images used are self-drawn
skin = []
body = []
hair = []

f1 = Frame(root)
f2 = Frame(root)
f1.pack()

click_x = 0
click_y = 0

#functions

def picrew():  
    #adding the images into the arrays
    x = 1
    for i in range(3):
        skin.append("skin"+str(x)+".png")
        x = x+1
    x = 1
    for i in range(3):
        body.append("body"+str(x)+".png")
        x = x+1
    x =1
    for i in range(6):
        hair.append("hair"+str(x)+".png")
        x = x+1

    def close_login(): #closes welcome screen
        f1.destroy()
        f2.pack()

    #welcome screen
    welcome = PhotoImage(file="welcome.png")
    login = Button(f1, image=welcome, command=close_login)
    login.pack()

    #switch to home screen
    main = PhotoImage(file="main.png")
    home = Label(f2, image=main)
    home.pack()

    #makes randomized starting character
    canvas = Canvas(f2, width=1200, height=1200) #create layered canvas for character
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    rand1 = random.choice(skin)
    rand2 = random.choice(body)
    rand3 = random.choice(hair)
    
    rand_skin = PhotoImage(file=rand1)
    rand_body = PhotoImage(file=rand2)
    rand_hair = PhotoImage(file=rand3)

    canvas.create_image(600, 600, image=main)
    canvas.create_image(600, 600, image=rand_skin)
    canvas.create_image(600, 600, image=rand_body)
    canvas.create_image(600, 600, image=rand_hair)

    select_skin = rand1 #stores in variable for later
    select_body = rand2
    select_hair = rand3

    skin_final = rand_skin #stores in variable for later
    body_final = rand_body
    hair_final = rand_hair

    canvas.store_image = {} #stores images in a dictionary so they don't get deleted
    #this array is over here and not in init bc the canvas hasn't been created yet

    def change_skin(num):
        nonlocal select_skin, skin_final #making these nonlocal allows it to update outside of this small function

        num = int(num)
        select_skin = skin[num]
        skin_final = PhotoImage(file=select_skin)

        canvas.store_image["skin"] = skin_final #skin is the key to skin_final

        canvas.delete("all")

        canvas.create_image(600, 600, image=main)
        canvas.create_image(600, 600, image=skin_final)
        canvas.create_image(600, 600, image=body_final)
        canvas.create_image(600, 600, image=hair_final)
    
    def change_body(num):
        nonlocal select_body, body_final

        num = int(num)
        select_body = body[num]
        body_final = PhotoImage(file=select_body)

        canvas.store_image["body"] = body_final #body is the key to body_final

        canvas.delete("all")

        canvas.create_image(600, 600, image=main)
        canvas.create_image(600, 600, image=skin_final)
        canvas.create_image(600, 600, image=body_final)
        canvas.create_image(600, 600, image=hair_final)

    def change_hair(num):
        nonlocal select_hair, hair_final

        num = int(num)
        select_hair = hair[num]
        hair_final = PhotoImage(file=select_hair)

        canvas.store_image["hair"] = hair_final #hair is the key to hair_final

        canvas.delete("all")

        canvas.create_image(600, 600, image=main)
        canvas.create_image(600, 600, image=skin_final)
        canvas.create_image(600, 600, image=body_final)
        canvas.create_image(600, 600, image=hair_final)

    
    def click(event): #the main customizing part
        #tracking the click coordinates
        global click_x, click_y
        click_x = event.x #the event is the actual click
        click_y = event.y

        #custom skin tone
        if 810<=click_x<=965 and 285<=click_y<=430: #first box
            if select_skin==skin[0]:
                change_skin(1)
            elif select_skin==skin[1]:
                change_skin(2)
            elif select_skin==skin[2]:
                change_skin(0)

        #custom body
        if 810<=click_x<=965 and 455<=click_y<=600: #second box
            if select_body==body[0]:
                change_body(1)
            elif select_body==body[1]:
                change_body(2)
            elif select_body==body[2]:
                change_body(0)

        #custom hair
        if 810<=click_x<=965 and 620<=click_y<=765: #third box
            if select_hair==hair[0]:
                change_hair(1)
            elif select_hair==hair[1]:
                change_hair(2)
            elif select_hair==hair[2]:
                change_hair(3)
            elif select_hair==hair[3]:
                change_hair(4)
            elif select_hair==hair[4]:
                change_hair(5)
            elif select_hair==hair[5]:
                change_hair(0)
        
    canvas.bind("<Button-1>",click) #when left mouse button is click, runs the click function

    root.mainloop() 


#main
picrew()
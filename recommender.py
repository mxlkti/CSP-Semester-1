#Titus Lau
#Period 5
#02/21/25

#init
from PIL import Image
import requests
from io import BytesIO
import random
import time

selection = ["https://tinyurl.com/3w7tkkmf", #skullpanda aisling figure
"https://tinyurl.com/s2bhkazx", #hirono x le petit prince series figure
"https://tinyurl.com/yzvwu2yd", #peach riot bloody valentine figures
"https://tinyurl.com/ycke2j6y", #labubu time to chill plush doll
"https://tinyurl.com/4trexf43", #baby molly future painter firguine
]

#functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def popmart():
    print("Welcome to the Popmart Figure Recommender!")
    print(" ")
    time.sleep(1)
    print("Are you indecisive?")
    print("Do you keep walking around the store looking for what to get?")
    print("Look no further because the Popmart Figure Recommender has a solution!")
    time.sleep(0.8)
    print("To start, please enter 'spin' to get a figure recommendation!")
    while True:
        next=input("Enter 'spin' to start!")
        next=next.lower()
        if next=='spin':
            print(" ")
            print("Image generating...")
            time.sleep(1)
            print("Rearranging pixels...")
            time.sleep(1.5)
            print("Coloring photo...")
            print(" ")
            time.sleep(0.5)
            x=random.randint(0,4)
            open_image(selection[x])
            print(" ")
            if x==0:
                print("This is a SkullPanda figure!")
                print("This specific figure is called the Aisling Figure.")
                print("You can buy this figure from the Popmart website for $43.99.")
            elif x==1:
                print("This is a Hirono figure!")
                print("This specific figure is from the Hirono x Le Petit Prince series.")
                print("You can buy this blindbox from the Popmart website for $16.99.")
            elif x==2:
                print("This is a Peach Riot figure!")
                print("This specific figure is from the Bloody Valentine series.")
                print("You can buy this set of 3 from the Popmart website for $134.99.")
            elif x==3:
                print("This is a Labubu plus!")
                print("This specific plush is called Time to Chill.")
                print("You can buy this doll from the Popmart website for $69.99.")
            elif x==4:
                print("This is a Baby Molly figure!")
                print("This specific figure is called Future Painter.")
                print("You can buy this figurine from the Popmart website for $156.99.")
            print(" ")
            print("This picture came directly from the Popmart website.")
            print(" ")
            yn=input("Would you like another recommendation?")
            yn=yn.lower()
            if yn=="yes" or yn=="y":
                print("Program restarting...")
                time.sleep(1.5)
            if yn=="no" or yn=="n":
                print("Alright, thank you for playing!")
                break
        else:
            print("I didn't get that")
            print("Please try typing in 'spin'")
#main
popmart()

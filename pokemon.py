#Pokemon Game

#init
level=0
petname="Mysterious Pokeball"
name="Titus obviously"
day=0
import random
import math
save_file = "pokemon_game_save.txt"

#functions
def save_game():
    with open(save_file, "w") as file:  # Open the save file in write mode
        file.write(petname + "\n")
        file.write(name + "\n")
        file.write(str(level) + "\n")
        file.write(str(day) + "\n")
    print("Game saved successfully!")

def load_game():
    global petname, level, day, name
    try:
        with open(save_file, "r") as file:
            petname = file.readline().strip()
            name = file.readline().strip()
            level = int(file.readline().strip())
            day = int(file.readline().strip())
        print("Game loaded successfully!")
    except FileNotFoundError:
        print("No save file found. Start a new game!")
    except ValueError:
        print("Save file is corrupted. Start a new game!")

def ball():
    print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⣠⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣄⠀⠀⠀⠀
      ⠀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣆⠀⠀⠀
      ⠀⠀⣸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣆⠀⠀
      ⠀⢰⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡆⠀
      ⢀⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀
      ⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇
      ⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷
      ⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
      ⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿
      ⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿
      ⢻⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡇
      ⢸⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⠃
      ⠀⢻⣿⣿⡈⠻⢿⣿⣿⣷⣤⣄⣀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠛⠉⢀⣀⣀⡀⠉⠻⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⡿⠟⣿
      ⠀⠀⢿⣿⣷⠀⠀⠈⠛⠿⢿⣿⣿⣿⣷⣶⣤⣤⣾⣿⡿⠋⠀⣴⠞⠉⠁⠈⠙⠻⣆⠀⠹⣿⣿⣧⣤⣤⣶⣾⣿⣿⣿⡿⠟⠛⣿⣿⣾⠁⠀
      ⠀⠀⠈⢿⣿⣷⡀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⣿⣿⣿⡇⠀⢸⡃⠀⠀⠀⠀⠀⠀⢹⡇⠀⢻⣿⣿⣿⠿⠿⠟⠋⠉⠀⠀⠀⠀⢀⣾⣿⡿⠀⠀
      ⠀⠀⠀⠈⢿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣧⠀⠸⣧⡀⠀⠀⠀⠀⢀⡾⠃⢀⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡿⠁⠀⠀⠀
      ⠀⠀⠀⠀⠀⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⣄⠈⠛⠶⠦⠴⠶⠋⠁⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⠏⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⣦⣤⣤⣶⣾⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣾⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)

def eevee():
    print("""
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡤⠴⠚⠋⣉⣠⣤⠆⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠰⠋⠁⣠⣴⣾⣿⣿⡿⠃⣨⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠉⠀⣤⡴⣟⣿⣳⣿⣾⡿⠁⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⣧⠈⣉⠉⠁⠒⠂⠠⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⣤⣛⢧⣻⣽⡿⣯⣷⡿⠁⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠘⢧⠀⠄⠈⠀⠒⠠⠄⡀⠈⠑⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠤⣀⠀⠀⠀⠀⠀⣰⠃⠀⣾⣵⣾⣿⣿⣿⣿⣿⡟⢁⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠈⢳⡀⠢⠀⠀⠀⢄⠀⠉⠰⣤⣀⠹⢤⣄⠀⠀⠀⣀⠀⢺⡅⠀⠐⠚⠒⠾⡄⠈⢳⣶⢦⣄⣰⠇⢀⣾⣿⣿⣿⣿⣿⣿⣿⠟⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⢦⠀⠀
      ⠀⠀⠀⠱⣄⠑⣄⢀⠠⣑⢮⣳⣼⣿⣷⣆⡈⢣⡀⢘⡏⠉⠘⠛⢦⠀⠀⠀⠀⠀⠀⠀⠁⠈⢻⠏⢀⣾⣿⣿⣿⣿⣿⣿⠟⣣⣞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠘⠈⣥⠀
      ⠀⠀⠀⠀⠈⠳⣌⠻⢷⣿⣾⣿⣿⣿⣿⣿⣿⡄⣞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠁⠘⠋⣼⣿⣿⠿⢋⣱⡼⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠎⠀⠀⠀⢸⠄
      ⠀⠀⠀⠀⠀⠀⠈⠳⢦⣉⠛⠿⢿⣿⣿⣿⣿⣟⡲⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣶⣩⡶⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠴⠒⠋⠀⠀⠀⠁⠀⠀⡆
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠶⢤⣬⣉⣛⠻⣓⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡍⢻⡆⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠛⣈⠉⡐⢂⡜⡁⠀⠀⠀⠀⠀⠀⠀⢱
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⡻⠀⠈⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠴⢂⣤⡀⠀⠀⠘⢸⡇⠀⠀⠀⠀⢀⡴⠋⢅⠢⠑⡨⠀⠀⡑⢢⣊⡀⠄⡖⠀⠀⠀⠀⠀⢸
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⣤⠞⠇⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⢀⣆⠀⠀⠀⡏⠀⠀⢀⡴⢫⠔⡉⢄⠢⠑⡄⢃⠔⡠⢉⠡⡐⠌⣂⠠⡀⠀⠀⠀⢸
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⢰⣿⣤⣾⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣾⣧⠀⠀⠀⡇⠀⢀⡾⣙⢆⡣⢌⠰⢈⠡⡐⠌⡰⢀⠣⡐⠄⡃⢄⠂⠥⢀⠠⣚⡘
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⢸⣿⣿⣿⠀⠀⢀⣶⠀⠀⠀⠀⢿⢿⣿⡇⠀⢀⣰⡏⠴⣸⡏⡸⡎⡶⢁⠆⡁⢆⠁⡎⠠⡈⢠⠀⢇⡈⢠⠈⡄⢁⠴⢁⡇
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠈⠶⠿⠟⠀⠀⠀⠁⠀⠀⠀⡀⠈⠉⠉⠀⡄⠎⡼⠀⠀⠉⠻⣵⢣⡝⣣⠎⡰⠈⡔⠠⢃⠜⡠⢉⠤⡘⠄⢣⠘⠤⣉⠆⡇
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠓⠒⠉⠃⠒⠋⠁⢀⢠⠒⣍⠸⣸⠃⠐⠂⠤⢀⢹⣣⢞⡱⣎⠥⣃⠔⡡⢊⠤⠑⡌⠰⢠⠉⢆⡘⢒⠤⢺⠄
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⡀⣀⢀⡀⣀⠠⢄⡐⠦⡑⣊⢱⡤⠟⠁⠀⠀⠀⠀⠀⠙⢶⢫⢶⣍⡞⣜⢢⡕⢢⢌⡑⣨⢑⢢⡉⢦⡘⣅⢪⡟⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡁⠉⠒⡶⢬⣰⣁⣞⣠⣃⠶⠵⠚⠉⢣⠀⠀⠀⠀⠀⠀⠀⡀⢀⢣⢊⠹⢾⣥⡳⢞⡱⣎⡳⣥⢋⡦⣙⢦⡱⣬⠟⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⢡⢸⢸⢠⠃⠎⢷⡻⣭⠷⣭⢳⣎⠷⡜⢵⣪⠞⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡌⡜⢢⠉⡜⠸⣿⣾⣽⣎⡷⣮⠟⠞⠉⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠟⡘⢄⠣⢌⡑⣾⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣎⣠⢔⢣⣼⠎⡜⣠⠋⡴⣈⠽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠴⢋⠔⣠⢪⠿⣆⢣⠒⡤⢓⠴⣡⠖⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠷⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠋⠀⠁⠳⡌⣴⡏⠀⠉⠳⣭⣒⣭⠶⠏⡌⠡⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣤⠀⢀⠀⠀⠀⢠⠁⠀⠀⠀⠀⢰⡿⠁⠀⠀⠀⠀⢸⡏⣴⠡⣮⢁⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⢷⣾⡀⢰⣶⠆⠀⠀⠀⠀⠀⣘⠃⠀⠀⠀⠀⠀⠈⠳⣧⣘⣳⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣍⡞⣻⣟⡼⠁⠄⣀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠿⣷⠋⡝⠀⣂⡁⠛⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣞⣀⣸⠅⣈⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)

def leafeon():
    print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⢀⡴⠒⠋⠉⠉⣉⣁⠤⠖⢢⠟⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⣸⡀⠀⠀⠀⠀⢠⠋⠀⠀⢀⡴⠋⠁⠀⢀⡴⠃⠀⠀⠀
      ⠀⠀⠀⠀⠀⢀⢔⡿⠂⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢠⠳⡆⠀⠀⠀⢠⡃⠀⠀⠀⡜⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀
      ⠀⠀⠀⢀⠞⢡⠎⠀⠀⣯⡴⠒⠉⠉⠉⠑⠢⣄⠀⠀⠀⠀⠀⠀⠀⡴⠊⠀⠀⣸⠀⡇⠀⠀⣰⠃⠸⡀⠀⡸⠁⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀
      ⠀⠀⢠⠋⢀⡏⠀⢀⣴⠋⣀⡀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⡠⠒⠻⠄⠀⢠⣇⡀⡇⠀⢠⠇⠀⠀⠱⣀⠃⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀
      ⠀⢀⡷⠀⡼⡇⠀⠀⠀⡎⠉⠀⢭⣷⡀⠀⠀⠀⠀⣳⠀⣠⠎⠀⠀⠀⢀⣴⠏⠁⠀⠇⠀⢸⠀⠀⠀⠀⢻⠀⠀⠀⠀⠨⢇⠀⠀⠀⠀⠀⠀
      ⠀⡼⠀⢰⠃⢳⠀⠀⠰⡃⠀⠀⡼⢸⡅⠀⠀⠀⢀⡎⡴⠁⠀⠀⣠⠖⠉⡞⠀⢠⣼⠀⠀⠘⡄⠀⠀⠀⠸⡄⠀⠀⢀⡴⠉⠙⢦⡀⠀⠀⠀
      ⠀⣧⠀⡎⡆⢸⢀⣀⣼⡿⣄⡞⢀⠞⠁⠀⠀⣀⣾⡼⠥⢄⣠⠞⠁⠀⣸⠁⠀⢠⠏⠀⠀⠀⠘⢆⠀⠀⠀⠘⢦⡰⠋⠀⠀⠀⠀⠙⣄⠀⠀
      ⢠⣯⠀⡇⠀⢸⠀⢀⡟⠀⢘⡴⠁⠀⣀⠴⠊⠉⢿⡇⠀⢠⠏⠀⠀⢠⠇⠀⢀⡎⠀⠀⠀⠀⠀⠈⠣⡀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠸⡄⠀
      ⠀⢻⠀⢳⡀⢸⠐⡞⠀⠀⡜⠀⢠⠊⠁⠀⠀⠀⢸⠀⢁⡏⠀⢀⡴⠛⣶⣦⠞⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⣇⠀
      ⠀⠀⢣⡀⠳⣼⠀⠀⠀⠀⢧⢠⠃⠀⠀⠀⠀⠀⠀⠀⣼⡠⠖⢫⢀⣠⠼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⠷⠚⠂⠀⢳⠀⠀⠀⠀⠀⢹⠀
      ⠀⠀⠀⠙⣤⡘⠀⠀⠀⠀⠈⢯⠀⠀⠀⠀⠀⠀⠀⠀⠋⢀⣤⡔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠷⣄⣄⠀⠈⣇⠀⠀⠀⠀⣘⡆
      ⠀⠀⠀⠘⠣⣄⠀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⣠⢴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⡀⣸⠀⠀⠀⣨⠇⠀
      ⠀⠀⠀⠀⠀⠈⢣⣿⣟⣖⠀⠀⠀⠰⣸⣙⡆⣹⠃⠀⡼⢁⠜⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⣠⠟⠉⠓⠢⠻⣅⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⢏⠻⠿⠆⠀⠀⠀⠟⠲⠖⠋⠀⣴⢛⣡⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠼⠥⢄⣠⠞⠁⠀⠀⠀⢀⡴⠚⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠘⠢⣀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠛⠻⠭⣀⣀⠤⠖⠒⠉⠉⠁⠀⠉⠑⠢⣰⠋⠀⠠⠔⠊⠉⠙⠒⣀⡤⠖⠋⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢓⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⠦⠤⠤⠤⠖⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢘⡲⠐⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⢏⠉⠉⠁⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠤⠤⣨⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠸⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⡤⠴⠒⠛⠢⣀⠀⠀⠈⠢⣀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⣹⠆⠀⠀⣸⠗⠢⣄⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡠⠞⡀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⢠⡏⠀⠀⡇⠀⢀⡰⢧⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠶⣶⠏⠀⠀⢰⠸⣇⠀⠀⠀⠀⠀⣠⣷⣤⣀⣰⡟⠀⠀⢀⡷⠀⠀⢱⢤⡴⠽⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣏⠀⠀⠀⣬⣷⣜⣦⡀⠀⢰⣿⡿⣿⣿⣿⠟⠀⠀⠀⣼⠟⠒⢲⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠉⠙⢲⣾⣿⣿⠃⠈⠁⠀⠘⠿⠿⠿⠟⠁⠀⠀⠀⣿⡏⠀⢀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠁⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡛⠓⠺⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)

def evolve1():
      if level==10:
            global petname
            print(" ")
            eevee()
            print("WOOOOSH")
            print("Your Pokemon has evolved from a Pokeball to an Eevee!")
            name_change=input("Would you like to rename your pet?")
            if name_change=="yes" or name_change=="y":
                  petname=input("What would you like to name your Eevee?")
            else:
                  print("Level up your Pokemon to reach new evolutions!")

def evolve2():
      if level==20:
            global petname
            print(" ")
            leafeon()
            print("WOOOOSH")
            print("Your Pokemon has evolved from an Eevee to an Leafeon!")
            name_change=input("Would you like to rename your pet?")
            if name_change=="yes" or name_change=="y":
                  petname=input("What would you like to name your Leafeon?")
            else:
                  print("Level up your Pokemon to reach new evolutions!")
            print(" ")
      else:
            print(" ")

def menu():
    print("Welcome to My Pocket Pokemon!") #start
    print("You are a famous Pokemon trainer from a far away land.")
    print("Your task is to train a mysterious Pokeball found in the corners of the world.")
    name=input("What is your name?")
    print(" ")
    print("Welcome "+name+"!")
    petname=input("What is your Pokeball's name?")
    ball()
    print("Great! "+petname+" is ready to start training!")
    print(" ")
    print("Welcome to your gym: "+name+" Center Gym.")
    print("Here you can check the stats, train, and battle other Pokemon.")
    print(" ")
    print("To exit the game, enter 'stop'")
    print("To save the game, enter 'save'")
    print("To load a saved game, enter 'load'")
    print(" ")

    while True:
      global day
      global level
      day=day+1
      evolve1()
      evolve2()
      print("Day: "+str(day))
      print("What would you like to do today?")
      activity=input("You can train, check stats, or battle other Pokemon.")
      if activity=="train" or activity=="tra" or activity=="t":
            print(" ")
            print("In the training center we can feed, bathe, and spar with our Pokemon.")
            train_act=input("What would you like to do today?")
            if train_act=="feed" or train_act=="f":
                  print(" ")
                  print(petname+" was hungry and you fed it a berry.")
                  print(petname+" is well-fed.")
                  print("  Pokemon level increased by 10XP")
                  if level<10:
                       level=level+1
                  elif 10<=level<20:
                       level=level+0.5
                  elif 20<=level:
                       level=level+0.2
            elif train_act=="bathe" or train_act=="b":
                  print(" ")
                  print(petname+" was dirty and you gave it a bath.")
                  print(petname+" is squeaky-clean.")
                  print("  Pokemon level increased by 10XP")
                  if level<10:
                       level=level+1
                  elif 10<=level<20:
                       level=level+0.5
                  elif 20<=level:
                       level=level+0.2
            elif train_act=="spar" or train_act=="s":
                  print(" ")
                  print(petname+" trained all day with you in the gym.")
                  print(petname+" is getting stronger.")
                  print("  Pokemon level increased by 10XP")
                  if level<10:
                       level=level+1
                  elif 10<=level<20:
                       level=level+0.5
                  elif 20<=level:
                       level=level+0.2
            else:
                  print(" ")
                  print("I didn't get that, try typing 'feed' or 'spar'.")
                  print(petname+" decided to rest for today and took a nap.")

      elif activity=="stats" or activity=="check" or activity=="check stats" or activity=="stat":
            if level>10:
                  ball()
            elif 10>=level>20:
                  eevee()
            else:
                  leafeon()
            print("Your Pokemon's current level is "+str(math.floor(level))+".")
            if level<20:
                 print("Level up your Pokemon to reach new evolutions!")
            print(petname+" played in the gym while you researched their level.")

      elif activity=="battle" or activity=="bat" or activity=="b":
            if level<3:
                  print("Please try leveling up your pet to level 3 to battle.")
                  print("Your Pokemon, looking defeated, did some pushups in protest.")
            else:
                  print("Welcome to the Arena Gym.")
                  print("Here you can battle other Pokemon.")
                  print(" ")
                  print("A new challenger has arrived!")
                  opp=random.randint(1,3)
                  if opp==1:
                        opp_name="Pikachu"
                  elif opp==2:
                        opp_name="Bulbasaur"
                  elif opp==3:
                        opp_name="Squirtle"
                  print("Let's welcome "+opp_name+" to the ring!")
                  for i in range(3):
                        dialouge=random.randint(1,7)
                        if dialouge==1:
                             print(petname+" pulled "+opp_name+"'s hair, looks like they were wearing a wig.")
                        elif dialouge==2:
                             print(opp_name+"came up from behind and jumped "+petname+".")
                        elif dialouge==3:
                             print(petname+" did a flip. 0 damage but looked cool.")
                        elif dialouge==4:
                             print(petname+" ran over "+opp_name+" with their Tesla Cybertruck. Yikes.")
                        elif dialouge==5:
                             print(opp_name+" has gun. RUN!")
                        elif dialouge==6:
                             print(petname+"? Where did you get a bomb-")
                        elif dialouge==7:
                             print(opp_name+" set the stadium on fire, everybody stop, drop, and roll!")
                  print(" ")
                  win=random.randint(1,2)
                  if win==1:
                        print(petname+" has won the gym battle!")
                        print("Congratulations!")
                        print("  Pokemon level increased by 20XP")
                        if level==9:
                             level=level+1
                        elif level<10:
                              level=level+2
                        elif 10<=level<20:
                              level=level+1
                        elif 20<=level:
                              level=level+0.4
                  if win==2:
                        print(opp_name+" has won the gym battle!")
                        print(petname+" still had a fun time.")
                        print("  Pokemon level increased by 10XP")
                        if level<10:
                              level=level+1
                        elif 10<=level<20:
                              level=level+0.5
                        elif 20<=level:
                              level=level+0.2

      elif activity=="stop":
            print(" ")
            print("Thank you for playing! We hope to see you again!")
            break
      elif activity=="save":
            save_game()
      elif activity=="load":
            load_game()
      else:
            print(" ")
            print("I didn't get that, try typing stats, train, or battle.")
            print(petname+" decided to rest for today and took a nap.")

#main
menu()

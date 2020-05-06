import os
import time
import datetime as datetime
from datetime import date

print("My Name is Eli, and i am your virtuel assistent")
input("Press Enter to continue...")
global client_name
client_name = str(input("What is your name?: "))
print("Hello",client_name,"now i will be introducing you to the commands")
input("Press Enter to continue...")
os.system("clear")


def main():

    #print the modes
    print("""
    1: Dino run game
    2: Advanced calculator
    3: Messenger tool
    4: Analyse stocks
    5: Current time
    6: Gomoku game
    7: Pacman game
    8:
    9:
    """)
                     
            
    mode = int(input("what mode do your want to use?: "))

    while mode == 1:
        print("You chose: Dino Run game")
        modules.dino_game()

    if mode == 2:
        print("You chose: Advanced calculator")
        modules.advanced_calc()

    if mode == 3:
        print("You chose: Messenger tool")
        modules.messenger_bot()

    elif mode == 4:
        print("You chose: Analyse stocks")
        modules.stock_graph()

    elif mode == 5:
        print("You chose: Current time")
        modules.current_datetime()

    elif mode == 6:
        print("You chose: Gomoku game")
        modules.gomoku_game()

    elif mode == 7:
        print("You chose: Pacman game")
        modules.pac_man()

    elif mode == 8:
        print("You chose: ")
        function7()

    elif mode == 9:
        print("You chose: ")
        function8()



class modules():
    
    def dino_game():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/Dino_game')
            os.system('python dino.py')
            #execfile("dino.py")
            main()    

    def advanced_calc():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/Advanced_calc')
            os.system('python advancedcalc.py')
            #execfile("dino.py")
            main()    

    def messenger_bot():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/Mesenger_bot')
            os.system('python3 fbot.py')
            main()

    def stock_graph():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/Stock_graph')
            os.system('python3 Stock.py')
            main()

    def current_datetime():
            now = datetime.datetime.now()
            print ("Current date and time : ")
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            main()

    def gomoku_game():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/gomoku_game')
            os.system('python3 gomoku.py')
            main()

    def pac_man():
        for i in range(1):
            os.chdir('/Users/adamkatborg/Desktop/Va-Procect/Modules/pac_man')
            os.system('python3 pac.py')
            main()





main()
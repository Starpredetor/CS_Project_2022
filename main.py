from utils import game
from db_connector import login, signup, get_points, get_lb , checkdb
import time
flag = False
def m_login(username, password):
    if login(username, password):
        global flag 
        flag = True
        return username
    else:
        flag = False
        return 
if checkdb():
    while True:
        time.sleep(0.5)
        print("--------------------")
        print("Starting up....")
        print("--------------------")
        time.sleep(1)
        print("""Please choose 
                 1. Login   
                 2. Sign up 
                 3. Exit""")
        ch = int(input("Enter your choice: "))
        print("--------------------")
        if ch == 1:
            print("Login")
            usrname = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                player = m_login(usrname, password)
            except:
                print("--------------------")
                print("Invalid login credientials please try again!")
                print("--------------------")
                continue
            while True:
                if player == False:
                    print("Couldn't login")
                    break
                else:
                    print("Game menu")
                    print("--------------------")
                    print("Enter 1 to start a new game.")
                    print("Enter 2 to get your current points.")
                    print("Enter 3 to get local learderboard.")
                    print("Enter 4 to log out.")
                    print("Enter 5 for help.")
                    print("--------------------")
                    m_ch = int(input("Enter your choice: "))
                    if m_ch == 1:
                        print("Starting a new game...")
                        print("--------------------")
                        game(flag, player)
                    elif m_ch == 2:
                        points = get_points(player)
                        print("--------------------")
                        print(f"Your current points are: {points}")
                        print("--------------------")
                        time.sleep(3)
                    elif m_ch == 3:
                        lb = get_lb()
                        print("--------------------")
                        print("Username        Score")
                        for i in lb:
                            print(i[0],"      ", i[1])
                        print("--------------------")
                        time.sleep(3)
                    elif m_ch == 4:
                        print("Logging out...")
                        print("--------------------")
                        break
                    elif m_ch == 5:
                        print("--------------------")
                        print("Enter 1 to start a new game.")
                        print("Enter 2 to get your current points.")
                        print("Enter 3 to get local learderboard.")
                        print("Enter 4 to exit the game.")
                        print("Enter 5 for help.")
                        print("--------------------")
                    else:
                        print("Invalid input enter 6 to get help.")
        elif ch == 2:
            print("Sign up...")
            usrname = input("Enter your username: ")
            password = input("Enter your password: ")
            signup(usrname, password)
            continue
        elif ch == 3:
            print("--------------------")
            print("Exiting the game...")
            print("--------------------")
            break
        else:
            print("Invalid input please choose from [1, 2 or 3].")
            continue
else:
    exit()
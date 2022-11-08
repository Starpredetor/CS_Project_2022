#Only run this file once before execution of the main file
import mysql.connector
import time
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.exists(os.path.join(THIS_FOLDER, 'dbpass.txt'))
print("---------------------------------")
print("Starting setup for Quiz Generator....")

print("---------------------------------")
time.sleep(3)

passw = input("Enter the default database password for this machine: ")
conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="")
if not my_file:
    with open("dbpass.txt", "w+") as f:
        if f.read() == "":
            f.write(passw)
        else:
            pass
    

cur = conn.cursor()
print("---------------------------------")
try:
    cur.execute("CREATE DATABASE QUIZDB")
    print("Creating Database...")
    time.sleep(3)
except mysql.connector.Error as err:
    print("Couldnt Create Database due to: ", err.msg)
else:
    print("Created database Successfully")

cur.execute("USE QUIZDB")
print("---------------------------------")
try:
    cur.execute("CREATE TABLE USERS (ursno int not null auto_increment, username varchar(50) not null unique, password varchar(50) not null, points int default 0, PRIMARY KEY(ursno))")    
    print("Creating Table...")
    time.sleep(3)

except mysql.connector.Error as err:
    print("Couldnt Create table due to: ", err.msg)
else:
    print("Created table Successfully")

print("Finalizing the files....")
time.sleep(2)

print("---------------------------------")
print("Set up successful...")
print("To start the game run the main file.")
print("Press enter to close the setup")
print("---------------------------------")
input()


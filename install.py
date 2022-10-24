#Only run this file once before execution of the main file
import mysql.connector
import time

print("---------------------------------")
print("Starting setup for Quiz Generator....")

print("---------------------------------")
time.sleep(3)

passw = input("Enter the default database password for this machine: ")
conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="")
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


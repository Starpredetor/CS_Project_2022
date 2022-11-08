import mysql.connector
import re

try:
    with open("dbpass.txt") as f:
        l = f.readlines()
        passw = re.sub("\n","", l[0])
except Exception as e:
    print(e)
    print("Run the Install file to fix this")
    print("Press any key to close")
    input()
    exit("Run install file")

def login(username, password):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"select * from users where username = '{username}' and password = '{password}'")
    except mysql.connector.Error as err:
        print("Couldn't log in due to : ", err.msg)
    data = cur.fetchall()
    if data[0][1] == username and data[0][2] == password:
        conn.close()
        return True
    else:
        conn.close()
        return False
      
    
def signup(username, password):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"insert into users values(default,'{username}', '{password}', 0)")
    except mysql.connector.Error as err:
        print("Couldn't sign up due to : ", err.msg) 
        return False
    else:
        print(f"User created with Username: {username} and password: {password}")
        conn.commit()
        conn.close()


def update_points(username, points):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"select * from users where username = '{username}'")
        val = cur.fetchone()
        new_pts = val[3]+points
        cur.execute(f"update users set points = {new_pts} where username = '{username}'")
    except mysql.connector.Error as err:
        print("Couldn't update points due to : ", err.msg)
        return False
    else:
        conn.commit()
        conn.close()



def get_points(username):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"select points from users where username = '{username}'")
        data = cur.fetchone()
    except mysql.connector.Error as err:
        print("Couldn't fetch points due to : ", err.msg)
    else:
        conn.commit()
        conn.close()
    return data[0]

def get_lb():
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"select username, points from users order by points desc")
        data = cur.fetchall()
        result = []
        for i in data:
            result.append(i)
    except mysql.connector.Error as err:
        print("Couldn't fetch points due to : ", err.msg)
    else:
        conn.commit()
        conn.close()
    return result

def checkdb():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
        cur = conn.cursor()
    except mysql.connector.ProgrammingError:
        print("--------------")
        print("No database found please run the install file to fix this.")
        print("--------------")
        return False
    else:
        return True
import mysql.connector

passw = "mypass"

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
        cur.execute(f"insert into users values(default,'{username}', '{password}', 0, 0.0)")
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
        print("Update succesful")
        conn.commit()
        conn.close()

def update_accuracy(username, accuracy):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"update users set points = {accuracy} where username = '{username}'")
    except mysql.connector.Error as err:
        print("Couldn't update points due to : ", err.msg)
        return False
    else:
        print("Update succesful")
        conn.commit()
        conn.close()

def get_accuracy(username):
    conn = mysql.connector.connect(host="localhost", user="root", password=passw, database="quizdb")
    cur = conn.cursor()
    try:
        cur.execute(f"select points from users where username = '{username}'")
        points = 0
    except mysql.connector.Error as err:
        print("Couldn't update points due to : ", err.msg)
        return False
    else:
        print("Update succesful")
        conn.commit()
        conn.close()

def get_points(username):
    pass

def get_lb():
    pass
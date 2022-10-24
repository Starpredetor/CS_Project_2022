from utils.db_connector import  update_points
import time
import re

def check_login(flag):
    if flag == True:
        return True
    else:
        return False

def game(flag,player):
    if check_login(flag):
        qna = get_questions()
        questions = qna[0]
        answers = qna[1]
        counter = 0
        user_answers = []
        while counter != len(questions):
            print("--------------")
            print("The question is: ")
            print(questions[counter])
            answer = input("Enter your answer: ")
            user_answers.append(answer.lower())
            print("--------------")
            counter += 1
        print("Round completed. Evaluating points...")
        time.sleep(3)
        points = 0
        for i in range(len(user_answers)):
            if user_answers[i] == answers[i]:
                points+=1
                print("--------------")
                print("Question number", i+1, "✓")
                print("--------------")
            elif user_answers[i] != answers[i]:
                print("--------------")
                print("Question number" , i+1, "X")
                print("Your answer: ", user_answers[i])
                print("Correct answer: ", answers[i])
                print("--------------")
            time.sleep(0.5)
        print("--------------")
        print("You scored: ", points, "Out of : ", len(questions))
        print("--------------")
        time.sleep(5)
        update_points(player,points)
    else:
        return


def get_questions():
    file = open("questions.txt", 'r')
    lines = file.readlines()
    questions = []
    answers = []
    a = []
    for i in lines:
        line = i.split("|")
        questions.append(line[0])
        a.append(line[1].lower())
    for j in a:
        answers.append(re.sub("\n","", j))
    return questions, answers

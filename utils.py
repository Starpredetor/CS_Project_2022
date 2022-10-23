#import ....
def startup():
    pass

def check_login(flag):
    if flag == True:
        return True
    else:
        return False

def game(flag,topic):
    input("Hit enter to start.......")
    if check_login(flag):
        qna_dict = get_questions(topic)
        questions = qna_dict.keys()
        answers = qna_dict.values()
        counter = 0
        user_answers = []

        while counter != len(questions):
            print("The first question is: ")
            print(questions[counter])
            answer = input("Enter your answer: ")
            user_answers.append(answer)

        points = 0
        for i in user_answers:
            if i == answers[user_answers.index(i)]:
                points+=1
                print("Question number", answers.index(i), "✓")
                print("--------------")
            elif i != answers[user_answers.index(i)]:
                print("Question number" , user_answers.index(i), "X")
                print("Your answer: ", i)
                print("Correct answer: ", answers[user_answers.index(i)])
                print("--------------")
        print("You scored: ", points, "Out of : ", len(questions))

        update_user_score(points)
        update_user_accuracy(points, len(questions))
    else:
        return

def update_user_score(score):
    #upload to db
    pass
def update_user_accuracy(correct, total):
    accuracy = total - correct/total
    #upload to db
    pass
def show_leaderboard():
    #get from db
    pass
def get_questions(topic):
    #get from txt files
    pass

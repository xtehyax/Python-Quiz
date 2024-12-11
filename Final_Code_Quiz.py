#Imports
import json
import random
import requests
from urllib.parse import unquote

quiz = []
correct_answers = 0

class Question:
    def __init__ (self, question, correct_answer, incorrect_answers, index):
        self.question_text = unquote(question)
        self.question_number = index

        options = ["A", "B", "C", "D"]
        self.correct_answer = random.choice(options)

        # correct option is storing one of A,B,C,D randomly
        self.answers_dict = {}
        # loop through A,B,C,D

        for option in options:
            if option == self.correct_answer:
                self.answers_dict[option] = unquote(correct_answer)
            else:            
                incorrect_answer = random.choice(incorrect_answers)
                self.answers_dict[option] = unquote(incorrect_answer)
                incorrect_answers.remove(incorrect_answer)
        
        #print(self.answers_dict)
 
    def __repr__(self):
        answers = ""
        for answer in self.answers_dict:
            answers += f"{answer}: {self.answers_dict[answer]}\n"
        return f"Question {self.question_number}: {self.question_text}\n{answers}"

print("Hello! Welcome to Anna & Josh's random trivia quiz. Type A, B, C or D to tell us your answer!")
question_amount = input("How many questions do you want in your quiz? ")


#Loading questions from JSON and putting into a list
response = requests.get(f"https://opentdb.com/api.php?amount={question_amount}&type=multiple&encode=url3986")
response_json = response.json()
questions_json = response_json["results"]
#print(questions_json)

for question_json in questions_json: 
    quiz.append(Question(question_json["question"], question_json["correct_answer"], question_json["incorrect_answers"], len(quiz) + 1))


for question in quiz:
    question_answer = input(question)
    if question_answer.lower() == question.correct_answer.lower():
        print("Well Done!")
        correct_answers += 1
    else: 
        print("Not quite right!")

if correct_answers == 0:
   print(f"You got {correct_answers} out of {len(quiz)}. Go you, dumb-ass!")
else:
    print(f"You got {correct_answers} out of {len(quiz)}. Go you, smarty pants!")
 


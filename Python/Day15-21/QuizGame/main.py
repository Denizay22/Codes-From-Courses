# TODO for future denizay:
# make a menu for selecting question type, number, and difficulty.
# there is 2 \n printed after each question because of html2text. remove them if possible.(tried strip() already)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))
    # print(question_bank[len(question_bank)-1].text + " " + question_bank[len(question_bank)-1].answer)

quiz = QuizBrain(question_bank)

i = 0
while i < len(question_bank):
    quiz.next_question()
    i += 1

print(f"You've completed the quiz. Your final score was {quiz.score}/{quiz.question_number}.")

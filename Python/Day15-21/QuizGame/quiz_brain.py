from html2text import html2text

class QuizBrain:
    questions_list = []

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = question_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(html2text(f"Q.{self.question_number + 1}:"
                                      f" {current_question.text} True or False?: ".strip())).lower()
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong!!")
            print(f"Correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number+1}\n")

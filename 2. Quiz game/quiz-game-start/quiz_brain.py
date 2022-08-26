class QuizBrain:
    score = 0

    def __init__(self, question_list: list, question_number=0):
        self.question_number = question_number
        self.question_list = question_list

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right.")
            QuizBrain.score += 1
            print(f"Your score is : {QuizBrain.score}/{self.question_number}")
        else:
            print("You are wrong.")
            print(f"Your score is : {QuizBrain.score}/{self.question_number}")

    def next_question(self):
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number} : {self.question_list[self.question_number - 1].text} (True/False)?: "
        )
        self.check_answer(user_answer, self.question_list[self.question_number - 1].answer)

    def still_has_questions(self):
        if self.question_number + 1 > len(self.question_list):
            return False
        else:
            return True

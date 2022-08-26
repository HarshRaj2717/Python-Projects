from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    new = Question()
    new.text = i["text"]
    new.answer = i["answer"]
    question_bank.append(new)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\n========================\nThe quiz has ended, your score is : {QuizBrain.score}/{quiz.question_number}")

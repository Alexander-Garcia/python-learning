from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for qd in question_data:
    question_bank.append(Question(qd["text"], qd["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

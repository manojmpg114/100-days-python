from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    # question_bank.append(Question(data["text"],data["answer"]))
    question_bank.append(Question(data["question"], data["correct_answer"]))

# print(question_bank)

for questions in question_bank:
    print(questions.text + "\n" + questions.answer + "\n")
    
quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():    #if quiz still has questions
    quiz.next_question()

print(f'Final score: {quiz.score}/{len(question_bank)}')
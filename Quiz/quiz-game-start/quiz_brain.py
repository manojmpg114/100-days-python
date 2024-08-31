class QuizBrain: #remember classes are created with the class leading term -- not def class, we def methods like __init__ 
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"{self.question_number +1}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1
        
    def still_has_questions(self):
        # self.state = True
        # if self.question_number == len(self.question_list):
        #     self.state = False
        # return self.state
        return self.question_number < len(self.question_list) #instead of having an if statement and knowing the result only gives T/F we can just return the condition
    
    def check_answer(self, user_answer,curr_questions_answer):
        self.user_answer = user_answer
        if curr_questions_answer.lower() == self.user_answer.lower():
            print('Correct!')
            self.score += 1
        else:
            print('Wrong!')
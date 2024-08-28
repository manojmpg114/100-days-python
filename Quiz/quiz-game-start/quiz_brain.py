class QuizBrain: #remember classes are created with the class leading term -- not def class, we def methods like __init__ 
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"{self.question_number}: {current_question.text} (True/False) ")
        
    def still_has_questions(self):
        self.state = True
        if self.question_number == len(self.question_list):
            self.state = False
        return self.state
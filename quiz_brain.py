#asking the next question
#checking if the user was right
#see if the game is at the end

class QuizBrain:


    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        save_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(save_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower().strip():
            print("You got the answer right.")
            self.score += 1
        else:
            print("Your answer is wrong.")
        print(f"The correct answer was: {correct_answer};")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
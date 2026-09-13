""" class dictating elements of the quiz """
class QuizBrain:
    """ constructor for attributes """
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.prompt = ''
        self.current_question = ''
    def still_has_questions(self):
        """ checking is the user still has more questions to go """
        return len(self.questions_list) != self.question_number
# asking the questions
    def next_question(self):
        """ displaying the next question """
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        self.prompt = input(f"Q.{self.question_number}: {self.current_question.text} "
                            "(True/False): ").capitalize()
        self.check_answer(self.prompt, self.current_question.answer)
# checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        """ checks that the answer was correct and shows score """
        if self.still_has_questions():
            if user_answer == correct_answer:
                print("You got it right!")
                self.score += 1
            else:
                print("That's wrong.")
            print(f"The correct answer was {correct_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
            print("\n")
    def final_score(self):
        """ shows final score when all questions are completed """
  # checking if we're at the end of the quiz
        print("\n")
        print("You've completed the quiz!")
        print(f"Final score is {self.score}/{self.question_number}")

""" defining the question class"""

class Question:
    """ constructor to set attributes """
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("2+3=5", "True")

# texting it works
# print(new_q)

# print(new_q.text)
# print(new_q.answer)

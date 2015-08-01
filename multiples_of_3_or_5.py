# Take in a number and solves it for the 1st project euler problem
class Euler1:
    def __init__(self, starting_num):
        self.starting_num = starting_num
        self.multiples = [num for num in range(1, self.starting_num)
                          if (num % 5 == 0) or (num % 3 == 0)]

    def get_answer(self):
        return sum(self.multiples)

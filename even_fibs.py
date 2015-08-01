# Takes in a number and solves project euler problem 2 for that number.
class Euler2():

    def __init__(self, limit):
        self.limit = limit
        self.fibs = self.get_fibo_secquence()
        self.even_fibs = self.get_even_fibs()
        self.answer = self.get_answer()

    def get_fibo_secquence(self):
        a, b = 1, 1
        fibs = []
        while True:
            a, b = b, a + b
            if a > self.limit:
                break
            fibs.append(a)
        return fibs

    def get_even_fibs(self):
        evens = [num for num in self.fibs if num % 2 == 0]
        return evens

    def get_answer(self):
        return sum(self.even_fibs)

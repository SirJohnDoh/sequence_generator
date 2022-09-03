from generator import Generator


class Fibonacci(Generator):
    results = {
        0: 0, 1: 1
    }

    def number(self, n: int):
        if n not in self.results:
            self.results[n] = self.number(n-1) + self.number(n-2)
        return self.results[n]

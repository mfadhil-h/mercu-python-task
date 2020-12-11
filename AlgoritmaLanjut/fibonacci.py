class Fibonacci:
    def __init__(self):
        self.fibcount = 10
        self.firstfib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def fib(self, n):
        if n <= self.fibcount:
            return self.firstfib[n - 1]
        else:
            for i in range(self.fibcount, n):
                self.firstfib.append(self.firstfib[-2] + self.firstfib[-1])
            self.fibcount = n
            return self.firstfib[-1]

    def fiblist(self, n):
        if n <= self.fibcount:
            return self.firstfib[:n]
        else:
            self.fib(n)
            return self.firstfib


fibonacci = Fibonacci()
for f in fibonacci.fiblist(25):
    print f

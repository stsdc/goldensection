import math

class Algorithm:
    def __init__(self):
        self.golden  = (math.sqrt(5.0) + 1.0)/2
        self.tolerance = 0.1

        self.a = -5
        self.b = 5

        self.c = self.b - (self.b - self.a) / self.golden
        self.d = self.a + (self.b - self.a) / self.golden

        self.f = lambda x: x*x + x + 1


    def step(self):
        if self.f(self.c) < self.f(self.d):
            self.b = self.d
            self.d = self.c
            self.c = self.b - (self.b - self.a)/self.golden
        else:
            self.a = self.c
            self.c = self.d
            self.d = self.a + (self.b - self.a) / self.golden

    def find_min(self):
        while (abs(self.b - self.a) > self.tolerance):
            self.step()
        return (self.d, self.c)

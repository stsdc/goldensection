import math

class Algorithm:
    def __init__(self):
        self.golden  = (math.sqrt(5.0) + 1.0)/2
        self.tolerance = 0.01

        self.a = -5
        self.b = 5

        self.tempa = self.a
        self.tempb = self.b

        self.set_cd()

        self.f = lambda x: 4*x*x + 2*x + 6


    def step(self):
        if self.f(self.c) < self.f(self.d):
            self.tempb = self.d
            self.d = self.c
            self.c = self.tempb - (self.tempb - self.tempa)/self.golden
        else:
            self.tempa = self.c
            self.c = self.d
            self.d = self.tempa + (self.tempb - self.tempa) / self.golden

        print(self.d, self.c)


    def find_min(self):
        self.set_cd()
        if(self.tolerance > 0):
            while (abs(self.tempb - self.tempa) > self.tolerance):
                self.step()
            self.tempa = self.a
            self.tempb = self.b
            return (self.d, self.c)

    def set_cd(self):
        self.c = self.tempb - (self.tempb - self.tempa) / self.golden
        self.d = self.tempa + (self.tempb - self.tempa) / self.golden

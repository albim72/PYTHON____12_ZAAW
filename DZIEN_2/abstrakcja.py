from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,n):
        return f'metoda nieabstrakcyjna nr {n}'

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7 #ciało domyślne metody abstrakcyjnej


class Regular(Prototyp):

    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1002

    def policz_x(self):
        return super().policz_x() + self.y*3


r = Regular(4,7)
print(f'metoda policz() -> {r.policz()}')
print(f'metoda policz_x() -> {r.policz_x()}')
print(r.msg(545))

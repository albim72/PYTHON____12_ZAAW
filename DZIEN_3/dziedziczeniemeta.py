def logger(self,m,n):
    return f'{m}: {n}'

class MultiBases(type):
    def __new__(cls, classname, bases, attrs):
        if len(bases) > 1:
            raise TypeError('dostępne jest tylko jednodziedziczenie!')
        return super().__new__(cls, classname, bases, attrs)

    def __init__(self,classname, bases, attrs):
        self.logger = logger


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A):
    pass

class Ekstra:
    pass

b = B()
print(f"{b.logger(23,'informacja')}")

# class Test(Ekstra,B):
#     pass

def policz(self,x,y):
    return x-2*y

B.logger = policz
c = B()
print(c.logger(27,55))

class C(B):
    pass

d = C()
print(d.logger(5,6))

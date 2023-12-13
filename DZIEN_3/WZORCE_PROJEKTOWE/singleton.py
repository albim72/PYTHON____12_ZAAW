import math
print(math.pi)

class Kolor:
    def __call__(self,k,b):
        return 200*k-b


k = Kolor()

print(k)
print(k(4,5))

print("_"*20+"tworzenie Singleton" + "_"*20)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Regular:
    pass

r1=Regular()
r2=Regular()

print(r1==r2)
print(r1 is r2)
print(r1)
print(r2)
print(id(r1))
print(id(r2))

class Sng(metaclass=Singleton):
    def __init__(self,kolor):
        self.kolor = kolor

s1 = Sng("czerwony")
s2 = Sng("niebieski")

print(s1==s2)
print(s1 is s2)
print(s1)
print(s2)
print(id(s1))
print(id(s2))

print(s1.kolor)
print(s2.kolor)

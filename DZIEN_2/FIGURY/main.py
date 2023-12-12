from trojkat import Trojkat
from prostokat import Prostokat
from trapez import Trapez
from Kolo import Kolo

tr = Trojkat(5.6,6.8)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')
print("_"*50)

pr1 = Prostokat(4,4.7)
print(f'pole figury {pr1.__class__.__name__} wynosi: {pr1.policz_pole():.2f} cm2')
print("_"*50)

pr2 = Prostokat(4,4)
print(f'pole figury {pr2.__class__.__name__} wynosi: {pr2.policz_pole():.2f} cm2')
print(type(pr2))
print("_"*50)

trp = Trapez(8.2,6.3,4.4)
print(f'pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2')
print("_"*50)

kl = Kolo(5.5)
print(f'pole figury {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm2')
print("_"*50)

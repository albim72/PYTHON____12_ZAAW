import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f'{fn.__name__} została uruchomiona...')
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite

#fncomposite -> wrapper

class Notifies(type):
    def __new__(cls,clsname,bases,attrs):
        for name,value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[name] = notify(value)
        return super(Notifies,cls).__new__(cls,clsname,bases,attrs)

class MyMath(metaclass=Notifies):
    def multi(a,b,c):
        p=a*b*c
        print(p)
        return p

    def policz(self,x,y):
        w = x/y*100
        print(w)
        return w

    @property
    def differ(self):
        return 34342

MyMath.multi(5,3,4)
mm =MyMath()
mm.policz(4,5)

print(MyMath.differ)
print(mm.differ)

class Info(metaclass=Notifies):
    def intro(self):
        print('to jest kod: 234754327543745')

i = Info()
i.intro()

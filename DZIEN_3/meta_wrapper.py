from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'pełna nazwa metody: {func.__qualname__}')
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


class DebugMeta(type):
    def __new__(cls,clsname,bases,attrs):
        obj = super().__new__(cls,clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj
    
    def __init__(cls,clsname,bases,attrs):
        cls.fc = cls.fc
        
    def fc(cls):
        return "ważna informacja"
    
        

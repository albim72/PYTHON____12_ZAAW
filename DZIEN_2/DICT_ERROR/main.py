"""
    budowa słownika poprzez zadanie listy lub krotki z kluczami i wartościami
    ograniczenia: wartości słownika mogą być reprezentowane tylko poprzez typy: int i float
"""

from klasybledu import IntFloatValueError,KeyValueConstructError

class CustomIntFloatDict(dict):
    empty_dict = {}
    
    def get_dict(self):
        return self.empty_dict
    
    def __init__(self,key=None,value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float,)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)
                

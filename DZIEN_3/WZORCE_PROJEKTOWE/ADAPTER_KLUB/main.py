from external import Musician,Dancer

class Club:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'klub {self.name}'

    def organize_event(self):
        return "koncert muzyki z oprawą taneczną..."
    
class Adapter:
    def __init__(self,obj,adapted_methods):
        self.obj = obj,
        self.__dict__.update(adapted_methods)
        
    def __str__(self):
        return str(self.obj)

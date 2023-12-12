class UjemneN(Exception):
    def __init__(self,n):
        self.n=n
        
    def __str__(self):
        return (f'zosatała zadana wartośc n = {self.n}.'
                f'Wartość argumentu silnii nie może być ujemna!')

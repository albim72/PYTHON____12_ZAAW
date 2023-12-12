class PositiveTuple(tuple):
    def __new__(cls,*numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x>=0:
                pos_numbers.append(x)
            else:
                skipped+=1
        instance = super().__new__(cls,pos_numbers)
        instance._skipped = skipped
        return instance


posnb = PositiveTuple(9,4,5,-4,0,-56,23,1,2,-23,-3,34,0,9,4,9,-9,-3)
print(type(posnb))
print(posnb)
print(posnb._skipped)

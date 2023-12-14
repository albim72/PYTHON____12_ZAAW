class FootballTeamIterator:
    def __init__(self,members):
        self.members = members
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            val = self.members[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()
    
    

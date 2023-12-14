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

class FootballTeam:
    def __init__(self,members):
        self.memebers = members

    def __iter__(self):
        return FootballTeamIterator(self.memebers)


def main():
    members = [f'gracz{str(x)}' for x in range(1,23)]
    members = members + ['trener1','trener2','trener3','fizjoterapeuta','rzecznik']
    team = FootballTeam(members)
    team_it = iter(team)
    # while True:
    #     print(next(team_it))

    for member in team:
        print(member)


if __name__ == '__main__':
    main()

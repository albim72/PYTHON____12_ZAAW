from homework import Homework

print("________________ HOMEWORK _________________")
g = Homework()
g.grade = 95
assert g.grade == 95
print(f'ocena za projekt: {g.grade}')

from homework import Homework
from exam import Exam
from grade import ExamG
from weakgrade import ExamWG

print("________________ HOMEWORK _________________")
g = Homework()
g.grade = 95
assert g.grade == 95
print(f'ocena za projekt: {g.grade}')

print("________________ EXAM _________________")
ex = Exam()
ex.part_a_grade = 88
ex.part_b_grade = 65

assert ex.part_a_grade == 88
assert ex.part_b_grade == 65

print(f'egzamin -> część a: {ex.part_a_grade} punktów, '
      f'część b: {ex.part_b_grade} punktów')

print("________________ EXAMG _________________")
first = ExamG()
first.math_grade = 34
first.alg_grade = 46
first.prog_grade = 51

print(f'egzamin pierwszy termin-> matematyka: {first.math_grade}, algorymika: {first.alg_grade}, '
      f'programowanie: {first.prog_grade}')

sec = ExamG()
sec.math_grade = 55
sec.alg_grade = 80
sec.prog_grade = 67

print(f'egzamin poprawka-> matematyka: {sec.math_grade}, algorymika: {sec.alg_grade}, '
      f'programowanie: {sec.prog_grade}')

print('dane z archiwum - pierwszy termin')
print(f'egzamin pierwszy termin-> matematyka: {first.math_grade}, algorymika: {first.alg_grade}, '
      f'programowanie: {first.prog_grade}')

print("________________ EXAMWG _________________")

first = ExamWG()
first.math_grade = 34
first.alg_grade = 46
first.prog_grade = 51

print(f'egzamin pierwszy termin-> matematyka: {first.math_grade}, algorymika: {first.alg_grade}, '
      f'programowanie: {first.prog_grade}')

sec = ExamWG()
sec.math_grade = 55
sec.alg_grade = 80
sec.prog_grade = 67

print(f'egzamin poprawka-> matematyka: {sec.math_grade}, algorymika: {sec.alg_grade}, '
      f'programowanie: {sec.prog_grade}')

print('dane z archiwum - pierwszy termin')
print(f'egzamin pierwszy termin-> matematyka: {first.math_grade}, algorymika: {first.alg_grade}, '
      f'programowanie: {first.prog_grade}')

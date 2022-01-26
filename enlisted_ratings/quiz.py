import random
import os

ratings = ['AET', 'AMT', 'AST', 'BM', 'CS', 'DC', 'DV', 'EM', 'ET', 'GM', 'HST', 'IS', 'IT', 'ME', 'MK', 'MST', 'MU', 'OS', 'PA', 'SK', 'YN', 'IV']

total = len(ratings)

def ask(rating):
  os.system("{}.png".format(rating))
  input("")
  os.system('cls')
  print(rating)
  input("")
  os.system('cls')

random.shuffle(ratings)
os.system('cls')

for rating in ratings:
  print("{} questions remaining.".format(total))
  ask(rating)
  total-=1
  if total == 0:
    print("Quiz complete!")
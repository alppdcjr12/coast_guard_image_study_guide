import random
import os

flags = list("abcdefghijklmnopqrstuvwxyz")
flags += [
  "unaone",
  "bissotwo",
  "terrathree",
  "kartefour",
  "pantafive",
  "soxisix",
  "setteseven",
  "oktoeight",
  "novenine",
]
flags += ['answering', 'first_repeater', 'second_repeater', 'third_repeater']

total = len(flags)

def ask(flag):
  os.system("{}.png".format(flag))
  input("")
  os.system('cls')
  print(flag.replace("_", " "))
  input("")
  os.system('cls')

random.shuffle(flags)
os.system('cls')

for flag in flags:
  print("{} questions remaining.".format(total))
  ask(flag)
  total-=1
  if total == 0:
    print("Quiz complete!")
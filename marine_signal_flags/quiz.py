import random
import os

flags = list("abcdefghijklmnopqrstuvwxyz")
flags += [
  "nadazero",
  "unaone",
  "bissotwo",
  "terrathree",
  "kartefour",
  "pantafive",
  "soxisix",
  "setteseven",
  "oktoeight",
  "novenine",
  'answering',
  'first_repeater',
  'second_repeater',
  'third_repeater_commanding_officer_not_on_board',
  "SOPA_pennant",
  "prep_pennant",
  ]

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
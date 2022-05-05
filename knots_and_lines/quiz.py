import random
import os

knots_and_lines = [
  "square_knot",
  "bowline",
  "clove_hitch",
  "slip_clove_hitch",
  "double_becket_bend",
  "bitter_end",
  "bight",
  "turn",
  "round_turn",
  "standing_part",
  ]

total = len(knots_and_lines)

def ask(item):
  os.system("{}.png".format(item))
  input("")
  os.system('cls')
  print(item.replace("_", " "))
  input("")
  os.system('cls')

random.shuffle(knots_and_lines)
os.system('cls')

for item in knots_and_lines:
  print("{} questions remaining.".format(total))
  ask(item)
  total-=1
  if total == 0:
    print("Quiz complete!")
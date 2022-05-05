import os
from random import randrange
from datetime import time

def get_random_time():
  choice = randrange(0,10)
  if choice == 0:
    minute = str(randrange(0,59))
    return "00:" + minute if len(minute) == 2 else "00:0" + minute
  elif choice == 1:
    hour = str(randrange(0,23))
    return hour + ":00" if len(hour) == 2 else "0" + hour + ":00"
  else:
    return time(randrange(0,23), randrange(0,59)).strftime("%H:%M")

while True:
  os.system('cls')
  print(get_random_time())
  input()
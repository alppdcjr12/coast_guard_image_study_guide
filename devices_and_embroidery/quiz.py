import random
import os
from os.path import exists

ranks_and_rates = ["sr", "sa", "fa", "aa", "sn", "fn", "an", "po3", "po2", "po1", "cpo", "scpo", "mcpo", "cmc", "mcpocgr", "mcpocg", "ens", "ltjg", "lt", "lcdr", "cdr", "capt", "rdml", "radm", "vadm", "adm", "w-2", "w-3", "w-4"]

collar_device_paths = [["{}_cd.png".format(title), title] for title in ranks_and_rates]
shoulder_insignia_paths = [["{}_si.png".format(title), title] for title in ranks_and_rates]
lacing_paths = [["{}_l.png".format(title), title] for title in ranks_and_rates]

all_paths = collar_device_paths + shoulder_insignia_paths + lacing_paths

total = len(all_paths)

def ask(path_and_title):
  os.system('cls')
  if exists(path_and_title[0]):
      os.system(path_and_title[0])
      input("")
  else:
    return None
  print(path_and_title[1].upper())
  return True

random.shuffle(all_paths)
os.system('cls')

real_question = False
for path in all_paths:
  print("~{} remaining.".format(total))
  if real_question:
    input("")
  if ask(path):
    real_question = True
  else:
    real_question = False
  total-=1
  if total == 0:
    print("Quiz complete!")
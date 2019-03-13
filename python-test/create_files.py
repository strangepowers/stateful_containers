import time
import glob

open('1.txt', 'w')

def spli(x): return int(x.split(".")[0])

files = glob.glob("*.txt")
number = map(spli, files)
max_number = max(number)

max_number_inc = max_number + 1
while True:
  time.sleep(1)
  new_file_name = str(max_number_inc) + ".txt"
  print new_file_name
  max_number_inc = max_number_inc + 1
  open(new_file_name, 'w')
  print "passed"
 

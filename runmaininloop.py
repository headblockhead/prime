import os
import sys

val = 0
num = sys.argv[1]

while val < int(num) :
	val = val + 1
	os.system("python ./main.py " + str(val))

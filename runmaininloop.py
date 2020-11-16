import os
import sys

val = 0
num = sys.argv[1]
os.system('rm -rfvd ./output.txt')
os.system('rm -rfvd ./notprimes.txt')
os.system('rm -rfvd ./primes.txt')

while val < int(num) :
	val = val + 1
	os.system("python ./main.py " + str(val))

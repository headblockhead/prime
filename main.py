import sys

# Python program to check if  
# given number is prime or not 
  
num = int(sys.argv[1])
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           with open("output.txt", "a") as f:
            print(num)
            othermul = num / i
            print(num, "is not a prime number because it is a multiple of ",i, " and", str(othermul), file=f) 
           with open("notprimes.txt", "a") as f:
            print(num, "is not a prime number because it is a multiple of ",i, " and", str(othermul), file=f)
           break
   else: 
       with open("output.txt", "a") as f:
            print(num)
            print("                                                                                ", num , "is a prime number", file=f)  
       with open("primes.txt", "a") as f:
            print(num , "is a prime number", file=f)  
  
else: 
   with open("output.txt", "a") as f:
            print(num)
            print(num, "is not a prime number because it is 1", file=f)
   with open("notprimes.txt", "a") as f:
            print(num, "is not a prime number because it is 1", file=f) 

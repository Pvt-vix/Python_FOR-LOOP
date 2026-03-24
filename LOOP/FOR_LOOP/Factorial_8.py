#Write a Program to calculate the factorial of a given number , such as 5 

#Input : 5
#5! ---> 5*4*3*2*1 = 120

#Expected Output :120

n = int(input("Enter a Number:"))
factorial = 1
 
for i in range(1, n+1):
    factorial *= i

print(f"Factorial of {n} is : {factorial}")



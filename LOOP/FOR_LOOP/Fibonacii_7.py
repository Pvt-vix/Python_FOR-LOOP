#Write a program to print the first 10 terms of the Fibonacci Sequence

#Expected Output: 0 1 1 2 3 5 8 13 21 34 

#Hint : Each term in the Fibonacci sequence is the sum of the two preceding ones

a = 0
b = 1
print(a,b, end=" ")

for _ in range(10):
    next_term= a + b
    print(next_term, end=" ")
    a,b = b,next_term



#Write a Program to check if a given number ,such as 7,is a prime number

#Input : 7

#Expected Output : 7 is a Prime number

num = int(input("Enter a Number:"))
is_prime = True

for i in range(2, int(num ** 0.5 ) + 1 ):
    if num % i == 0:
        is_prime = False
        break

if is_prime  and num > 1:
    print(f"{num} is a Prime member")
else:
    print(f"{num} is Not a Prime member")

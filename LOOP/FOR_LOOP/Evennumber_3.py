#Write a program to print all even numbers from 1 to 10 

#Expected Output: 2 4 6 8 10

#num = int(input("Enter Number:"))

for i  in range(1,11):
    if i % 2 == 0 :
        print(i,end=" ")

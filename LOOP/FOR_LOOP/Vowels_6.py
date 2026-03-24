#Write a Program to count the number of vowels in the word "Education".
# Vowels --> a e i o u

#Input:Python

#Expected Output:1

vowels = "aeiou"
Words = "Python"
count = 0

for char in Words:
    if char in vowels:
        count += 1

print(f"Total vowels in {Words} is {count}")

#Write a program to count occurrences of each character in the word "programming"

#input:programming

word = input("Enter a Word:")
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char,count in char_count.items():
    print(char + ":", count) 
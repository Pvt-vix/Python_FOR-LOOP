#Write a Program to print the Word "Python" in reverse using a for loop

#Expected Output: nohtyP

word = input("Enter word:")
for i in range(len(word) - 1, -1,-1): 

    print(word[i], end=" ")
#Backwards Print

word = input("Enter a word to reverse: ")

for i in range(len(word), 0, -1):
    print(word[i-1], end=" ")

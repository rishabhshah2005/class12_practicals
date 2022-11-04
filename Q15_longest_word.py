# Q2. Program to take a list of words and print the longest word with the length.
words = []
for i in range(5):
    wrd = input(f"Enter word {i+1}: ")
    words.append(wrd)

long = ''
for i in words:
    if len(long)<len(i):
        long = i

print("The longest word is", long)

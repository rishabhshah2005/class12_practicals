# Q7. Read a text file and display the number of vowels/consonants/uppercase/lowercase
# characters in the file.

vow=['a','e','i','o','u','A','E','I','O','U']

f = open('sample.txt', 'r')
a = f.read()
f.close()

vowels = 0
cons=0
upper=0
lower=0

for i in a:
    if i in vow:
            vowels+=1
    elif i==' ':
        pass
    else:
        cons+=1
    
    if i.isupper():
        upper+=1
    elif i==' ':
        pass
    else:
        lower+=1

print('Vowels: ', vowels)
print('Consonants: ', cons)
print('Uppercase: ', upper)
print('Lowercase: ', lower)
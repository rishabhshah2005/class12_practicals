# Q14. Program that inputs a main string and then creates an encrypted string

shift = 5
letters = []
numbers = ['0','1','2','3','4','5','6','7','8','9']
hash = ''
for i in range(97, 123):
    letters.append(chr(i))

og_string = input("Enter string to encrypt: ")

def deter_ceaser(cha):
    if cha in letters:
        ind = letters.index(cha)
        if (ind+shift)<=len(letters)-1:
            new_ind = ind+shift
            return letters[new_ind]
        
        else:
            new_ind = (ind+shift)-len(letters)
            return letters[new_ind]

    if cha in numbers:
        ind = numbers.index(cha)
        if (ind+shift)>(len(numbers)-1):
            new_ind = (ind+shift)-len(numbers)
            return numbers[new_ind]
        else:
            new_ind = ind+shift
            return numbers[new_ind]
        
    
    else:
        return cha

for i in og_string:
    hash += deter_ceaser(i)

print("The ceaser cyhper is",hash)


# Q8. Remove all the lines that contain the character 'a' in a file and write it to another file.

f = open('some_lines_with_A.txt', 'r+')

text = f.readlines()
new=[]
for i in text:
    if 'a' in i:
        new.append(i)
        
inter=list(set(text)-set(new))

f.seek(0)
f.truncate()
f.writelines(inter)

f.close()

k = open("lines_with_only_A.txt", 'w')
k.writelines(new)
k.close()

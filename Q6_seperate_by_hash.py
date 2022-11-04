# Q6.Read a text file line by line and display each word separated by a #.

f = open('sample.txt', 'r')
a = f.read()
f.close()

splitted = a.split(' ')
print('#'.join(splitted))

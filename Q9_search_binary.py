# Q9 Create a binary file with name and roll number. Search for a given roll number and
# display the name, if not found display appropriate message.

import pickle

f = open("binary_data.dat", 'rb')
read = pickle.load(f)
f.close()

roll = int(input("Enter the rollno: "))
for i in read:
    if i[1] == roll:
        print("rollno.", i[1], "is", i[0])
        roll = True

if roll != True:
    print("rollno not found")

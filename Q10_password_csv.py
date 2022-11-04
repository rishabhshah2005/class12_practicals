# Q10. Create a CSV file by entering user-id and password, read and search the password
# for given user id.
import csv

f = open('sample_csv.csv', 'r')
read = csv.reader(f)

id = input("enter id: ")
for i in read:
    if i[0]==id:
        print("Password:", i[1])
        


f.close()

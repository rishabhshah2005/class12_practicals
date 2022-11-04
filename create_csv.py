import csv

f = open('sample_csv.csv', 'w', newline='')
lst = [['rishabh', 'hello123'], ['avi', 'passwaod'], ['jack', '2005_1234']]
file = csv.writer(f)
file.writerows(lst)
f.close()

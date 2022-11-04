import pickle

f = open("binary_data.dat", 'wb')
lst = [['rishabh', 24], ['mayank', 21], ['garv', 67], ['kohli', 12]]
pickle.dump(lst, f)
f.close()

import pickle

fp = open("note.dat", "rb")
i = pickle.load(fp)
print("讀取整數 = ", str(i))
str1 = pickle.load(fp)
print("讀取姓名 = ", str1)
list1 = pickle.load(fp)
print("讀取串列 = ", str(list1))
fp.close()    

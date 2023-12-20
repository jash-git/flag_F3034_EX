import pickle

fp = open("note.dat", "wb")
print("寫入整數: 11")
pickle.dump(11, fp)
print("寫入字串: '陳會安'")
pickle.dump("陳會安", fp)
print("寫入串列: [1, 2, 3, 4]")
pickle.dump([1, 2, 3, 4], fp)
fp.close()    



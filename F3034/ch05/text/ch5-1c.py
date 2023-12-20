import os

path = "./videos"
bname = "video"
count = 1
for fname in os.listdir(path):
    s_fname = os.path.join(path, fname)
    name  = os.path.splitext(fname)
    new_fname = bname + str(count) + name[1]
    count = count + 1
    new_fname = os.path.join(path, new_fname)
    print(s_fname, new_fname)
    os.rename(s_fname, new_fname)
    


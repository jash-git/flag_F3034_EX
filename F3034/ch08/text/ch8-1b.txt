import os, shutil

s_path = "./tmp"
d_path = "./videos"
if not os.path.isdir(d_path):
    os.mkdir(d_path)
for fname in os.listdir(s_path):
    s_fname = os.path.join(s_path, fname)
    d_fname = os.path.join(d_path, fname)
    shutil.copyfile(s_fname, d_fname)
    


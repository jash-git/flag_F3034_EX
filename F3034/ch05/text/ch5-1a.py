import os

path = "./tmp"
for fname in os.listdir(path):
    print(os.path.join(path, fname))


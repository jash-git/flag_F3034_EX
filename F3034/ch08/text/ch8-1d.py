import os

path = "./jpgs"
for root, dirs, files in os.walk(path):
    print(root)
    for fname in files:
        print(os.path.join(root, fname))
    


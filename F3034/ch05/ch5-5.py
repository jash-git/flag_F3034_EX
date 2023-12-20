import os, fnmatch
 
path = "./text"
keyword = "for"

for root, dirs, files in os.walk(path):
    for ext in ['txt', 'py', 'c']:
        for fname in fnmatch.filter(files, '*.' + ext):
            file = os.path.join(path, fname)
            with open(file, "r") as fp:
                num = 1
                for line in fp.readlines():
                    if keyword in line:
                        print("檔案: ", fname)
                        print(num, ":", str(line))
                    num = num + 1   
                    
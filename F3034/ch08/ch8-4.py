import os, re, fnmatch, docx
 
path = "./text"
pattern = re.compile('for|if') 

for root, dirs, files in os.walk(path):
    for ext in ['txt', 'py', 'c', 'docx']:
        for fname in fnmatch.filter(files, '*.' + ext):
            file = os.path.join(path, fname)
            if ext != "docx":
                with open(file, "r") as fp:
                    num = 1
                    for line in fp.readlines():
                        if re.search(pattern, line):
                            print("檔案: ", fname)
                            print(num, ":", str(line))
                        num = num + 1
            else:
                try:
                    doc = docx.Document(file)
                    num = 1
                    for p in doc.paragraphs:
                        if re.search(pattern, p.text):
                            print("檔案: ", fname)
                            print(num, ":", p.text)
                        num = num + 1
                except:
                    print("無法讀取Word檔案: ", file)
                  
                    
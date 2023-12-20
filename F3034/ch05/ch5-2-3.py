import os

os.makedirs("./img/a")
os.makedirs("./img/a/b")
os.makedirs("./img/a/b", exist_ok=True)

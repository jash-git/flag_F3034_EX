from pathlib import Path

path = Path("temp", "test.txt")
path.write_text("陳會安")
path.write_text("江小魚")
print("檔案內容:", path.read_text())

with path.open("a") as fp:
    fp.write("陳允傑")
print("檔案內容:", path.read_text())

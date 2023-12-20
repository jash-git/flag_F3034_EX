from pathlib import Path

path = Path("temp", "test.txt")
print(path)
print(path.exists())
path.touch()
print(path.exists())


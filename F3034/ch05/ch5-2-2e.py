from pathlib import Path

path = Path("temp", "test.txt")
path.unlink()
print(path.exists())



from pathlib import Path

path = Path("examples")
for item in path.iterdir():
    print(item)



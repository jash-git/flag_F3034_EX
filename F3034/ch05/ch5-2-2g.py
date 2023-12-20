from pathlib import Path

path = Path("examples", "圖片1", "ball0.jpg")
print(path)

path2 = Path("examples") / Path("圖片1") / Path("ball0.jpg")
print(path2)

print(Path("/temp") == Path("/temp"))
print(Path("/temp/a") == Path("/temp/b"))


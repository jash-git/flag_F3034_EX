from pathlib import Path
from datetime import datetime

path = Path("temp", "test.txt")
print("檔名:", path.name)
print("副檔名:", path.suffix)
print(path.stat())
print(path.stat().st_size)
print("建立日期:", datetime.fromtimestamp(path.stat().st_ctime))
print("存取日期:", datetime.fromtimestamp(path.stat().st_atime))
print("修改日期:", datetime.fromtimestamp(path.stat().st_mtime))
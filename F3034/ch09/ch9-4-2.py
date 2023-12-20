import requests
import shutil

fname = "2330TW.csv"
url = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=1625712846&period2=1657248846&interval=1d&events=history&includeAdjustedClose=true"

r = requests.get(url, stream=True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(fname, 'wb') as fp:
        shutil.copyfileobj(r.raw, fp)
    print("已經成功下載CSV檔案:", fname)

import requests
 
fname = "Youbike2.json"
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
 
r = requests.get(url)
if r.status_code == 200:
    r.encoding = "utf-8"
    with open(fname, 'w', encoding="utf8") as fp:
        fp.write(r.text)

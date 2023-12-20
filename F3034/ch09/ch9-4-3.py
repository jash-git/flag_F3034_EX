import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
csvfile = "2330TW.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        ws.append(row)
        
wb.save("2330TW.xlsx")
wb.close()

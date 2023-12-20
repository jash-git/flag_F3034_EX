import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
csvfile = "Sales.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        ws.append(row)
        
wb.save("CSV2Excel.xlsx")
wb.close()

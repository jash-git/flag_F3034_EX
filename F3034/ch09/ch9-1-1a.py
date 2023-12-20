from openpyxl import load_workbook
import csv

wb = load_workbook("營業額.xlsx")
ws = wb.active
csvfile = "營業額.csv"  
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    for r in ws.rows:
       row = []
       for cell in r:
           row.append(cell.value)
       writer.writerow(row)
 

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet.insert_rows(1, 3)
wb.save('example3.xlsx')



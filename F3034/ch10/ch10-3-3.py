import openpyxl

# 讀取Excel檔案
wb = openpyxl.load_workbook('customer_service.xlsx')
# 選擇第一個工作表
ws = wb.active

# 使用迴圈逐一顯示C2到C5的儲存格內容
for row in ws.iter_rows(min_row=2, max_row=5, min_col=3, max_col=3):
    for cell in row:
        print(cell.value)

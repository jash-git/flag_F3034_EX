from check_excel_file import check_excel_file

file_path = 'excel/example.xlsx'

if check_excel_file(file_path):
    print('檔案存在')
else:
    print('檔案不存在')

from win32com.client import Dispatch
import os

app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Open(os.getcwd()+"/ExcelVBA巨集程式.xlsm")
app.Application.Run("ExcelVBA巨集程式.xlsm!Hello")
result = app.Application.Run("ExcelVBA巨集程式.xlsm!Add", 10, 20)
print(result)
xlsx.Close(False)
app.Quit()
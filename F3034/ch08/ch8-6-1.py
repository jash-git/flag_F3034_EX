from win32com.client import Dispatch
import os

app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Open(os.getcwd()+"/營業額.xlsx")
sheet = xlsx.Worksheets[0]
sheet.ExportAsFixedFormat(0, os.getcwd()+"/營業額.pdf")
xlsx.Close(False)
app.Quit()
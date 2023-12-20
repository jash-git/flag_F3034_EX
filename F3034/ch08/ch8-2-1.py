from win32com.client import Dispatch
import os
import time

app = Dispatch("Word.Application")
app.Visible = 1
app.DisplayAlerts = 0
docx = app.Documents.Open(os.getcwd()+"/test.docx")
time.sleep(2)
docx.Close()
app.Quit()


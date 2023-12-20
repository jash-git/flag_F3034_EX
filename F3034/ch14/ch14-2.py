from openpyxl import load_workbook
from openpyxl.drawing.image import Image

wb = load_workbook("Hello.xlsx")
ws = wb.active

logo = Image("koala.png")

logo.height = 150
logo.width = 150

ws.add_image(logo, "A3")
wb.save("Hello_logo.xlsx")
wb.close()
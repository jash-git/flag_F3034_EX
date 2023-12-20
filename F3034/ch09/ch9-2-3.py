from docx2pdf import convert
import os

inputFile = os.getcwd()+"/PDF表格範例.docx"
outputFile = os.getcwd()+"/PDF表格範例.pdf"
file = open(outputFile, "w")
file.close()

convert(inputFile, outputFile)


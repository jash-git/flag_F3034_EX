from docx2pdf import convert
import os

inputFile = os.getcwd()+"/Word報告.docx"
outputFile = os.getcwd()+"/Word報告2.pdf"
file = open(outputFile, "w")
file.close()

convert(inputFile, outputFile)


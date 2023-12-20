import tabula

df = tabula.read_pdf("PDF表格範例.pdf", pages="all")
print(len(df))
for i in range(len(df)):
    df[i].to_excel("PDF表格範例"+str(i)+".xlsx")

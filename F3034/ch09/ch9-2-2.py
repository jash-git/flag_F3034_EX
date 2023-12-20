import pandas as pd
 
tables = pd.read_html("https://fchart.github.io/ML/test_table.html")
 
for i in range(len(tables)):
    df = tables[i]
    df.to_excel("HTML_table"+str(i)+".xlsx",
                       index=False,
                       engine="openpyxl")

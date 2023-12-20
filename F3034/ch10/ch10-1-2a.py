import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://fchart.github.io/test/ex3_03.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')

data = []
columns = []

for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th', 'td']):
        row_data.append(cell.text.strip())
        if len(columns) < len(row_data):
            columns.append(cell.text.strip())
    if row_data:
        data.append(row_data)

df = pd.DataFrame(data, columns=columns)
df.to_excel('sales.xlsx', index=False)

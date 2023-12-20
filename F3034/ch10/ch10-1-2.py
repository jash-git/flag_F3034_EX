import pandas as pd
import requests

url = 'https://fchart.github.io/iris.csv'
response = requests.get(url)

with open('iris.csv', 'wb') as f:
    f.write(response.content)

iris_data = pd.read_csv('iris.csv')
iris_data.to_excel('iris.xlsx', index=False)

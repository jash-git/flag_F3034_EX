import pandas as pd

products = {"分類": ["居家","居家","娛樂","娛樂","科技","科技"],
            "商店": ["家樂福","大潤發","家樂福","全聯超","大潤發","家樂福"],
            "價格": [11.42,23.50,19.99,15.95,55.75,111.55]}

ordinals =["A", "B", "C", "D", "E", "F"]        

df = pd.DataFrame(products, 
                  columns = ["商店", "價格"],
                  index = products["分類"]) 
print(df.T) 
df.T.to_html("ch13-2-1d.html")
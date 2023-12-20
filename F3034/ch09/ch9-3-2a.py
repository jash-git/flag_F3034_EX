import pandas as pd

ubike01 = pd.read_excel("Ubike01.xlsx",
                        engine="openpyxl")
print(ubike01.head())
ubike02 = pd.read_excel("Ubike02.xlsx",
                        engine="openpyxl")
print(ubike02.head())
ubike03 = pd.read_excel("Ubike03.xlsx",
                        engine="openpyxl")
print(ubike03.head())

df_list = [ubike01, ubike02, ubike03]
joined_df = pd.concat(df_list, axis=1)
joined_df.to_excel("Joined_Ubike_by_col.xlsx",
                   index=False,
                   engine="openpyxl")

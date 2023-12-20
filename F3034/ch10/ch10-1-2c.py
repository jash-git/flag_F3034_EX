import os
import pandas as pd

# 指定目錄路徑
directory = "ubike"

# 列出目錄下所有Excel檔案
excel_files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]

# 讀取所有Excel檔案並合併
dfs = []
for file in excel_files:
    filepath = os.path.join(directory, file)
    df = pd.read_excel(filepath)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

# 將合併後的結果寫入新的Excel檔案
output_filepath = os.path.join(directory, "Joined_Ubike.xlsx")
merged_df.to_excel(output_filepath, index=False)

print(f"合併完成，輸出檔案: {output_filepath}")

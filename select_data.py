import pandas as pd

ds = pd.read_csv("./data-cleaning/data_selected_clean.csv", encoding='utf-8')
print(len(ds))
english_only = ds[ds['english_only'] == True]
print(len(english_only))
english_only.to_csv("final_cleaned.csv")
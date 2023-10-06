import pandas as pd
import numpy as np

csv_file = pd.read_csv("new_data.csv", encoding='unicode_escape')
dataset = csv_file[['id','native','language','probabilities','english_only','text']]

# removing duplicates
print(f'Orginal Length: {len(dataset)}')
dup_removed = dataset.drop_duplicates(['native','language','text'])
print(f'New Length: \t{len(dup_removed)}')

#dup_removed.to_csv('new_data_clean.csv')
#ds = pd.read_csv("new_data_clean.csv", encoding='unicode_escape')

ds = dup_removed.copy()

# grouping dialects 
ds['native'].mask(ds['native'] == 'Basque<br/>Spanish', 'Spanish<br/>Basque', inplace=True)
ds['native'].mask(ds['native'] == 'Catalan<br/>Spanish', 'Spanish<br/>Catalan', inplace=True)
ds['native'].mask(ds['native'] == 'Galician<br/>Spanish', 'Spanish<br/>Galician', inplace=True)
ds['native'].mask(ds['native'] == 'Italian<br/>Spanish', 'Spanish<br/>Italian', inplace=True)


# filtering by language
la_list = ['Spanish<br/>Catalan','Spanish<br/>Galician',
'Spanish<br/>Basque','Spanish<br/>Italian', 'Italian', 'French','Spanish']
mask = ds['native'].isin(la_list)
dataset_selection = ds[mask]
print(len(dataset_selection))
print(dataset_selection['native'].value_counts())

dataset_selection.to_csv('data_selected_clean.csv')

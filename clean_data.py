import pandas as pd

csv_file = pd.read_csv("new_data.csv", encoding='unicode_escape')
dataset = csv_file[['id','native','language','probabilities','english_only','text']]

print(f'Orginal Length: {len(dataset)}')
dup_removed = dataset.drop_duplicates(['native','language','text'])
print(f'New Length: \t{len(dup_removed)}')


dup_removed.to_csv('new_data_clean')
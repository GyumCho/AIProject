import pandas as pd

csv_file = pd.read_csv("new_data.csv", encoding='unicode_escape')
dataset = csv_file[['id','native','language','probabilities','english_only','text']]

# removing duplicates
print(f'Orginal Length: {len(dataset)}')
dup_removed = dataset.drop_duplicates(['native','language','text'])
print(f'New Length: \t{len(dup_removed)}')


# selecting languages
mask = ((dup_removed['native'] == 'French') | (dup_removed['native'] == 'Spanish'))
dataset_selection = dup_removed[mask]
print(len(dataset_selection))

# count values
#print(dup_removed['native'].value_counts().to_string())
# dup_removed.to_csv('new_data_clean')
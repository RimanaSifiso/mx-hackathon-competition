import pandas as pd

df = pd.read_csv('../data/TrainData.csv')

valid_cell_prefixes = []

for cellprefix in df['cellprefix'].unique():
    if len(cellprefix) == 2:
            valid_cell_prefixes.append(cellprefix)
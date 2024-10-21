import pandas as pd
from datetime import datetime
file_path = 'fights.csv'
df = pd.read_csv(file_path)
df = df.drop(columns=['Location'])
df = df.drop(columns=['EmptyArena'])
print(df)
import pandas as pd
from datetime import datetime

fights = 'fights.csv'
fights = pd.read_csv(fights)
fights = fights.drop(columns=['Location'])
fights = fights.drop(columns=['EmptyArena'])

fighter_stats = 'stats.csv'
fighter_stats = pd.read_csv(fighter_stats)
fighter_stats['date'] = pd.to_datetime(fighter_stats['date_of_birth'], errors ='coerce')

today = datetime.today()
fighter_stats['age'] = fighter_stats['date'].apply(lambda dob: today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)))
fighter_stats = fighter_stats.drop(columns=['date_of_birth', 'date'])
# testing print chimaev
chimaev = fighter_stats.loc[fighter_stats['name'] == 'Khamzat Chimaev']
print(chimaev)
bobby = fighter_stats.loc[fighter_stats['name'] == 'Robert Whittaker']
print(bobby)
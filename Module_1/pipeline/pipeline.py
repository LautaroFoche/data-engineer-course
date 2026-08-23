import sys
import pandas as pd

month = sys.argv[1]

print('Month:', month)

df = pd.DataFrame({'day': [1, 2, 3], 'value': [4, 5, 6]})
df['month'] = month
print(df.head())

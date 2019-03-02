import pandas as pd

df1 = pd.read_csv("file_a.csv")
df2 = pd.read_csv("file_b.csv")

df = pd.merge(df1, df2, on='user_id')

df.to_csv('merged.csv')

print(df)
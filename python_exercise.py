import pandas as pd
import requests
from pandas.io.json import json_normalize
import json
import csv

# Reading original CSV files and merging into one CSV file

df1 = pd.read_csv("file_a.csv")
df2 = pd.read_csv("file_b.csv")
df = pd.merge(df1, df2, on='user_id')
#df.to_csv('merged_python.csv')
df.columns = ['uid','email','first_name','last_name']

# Taking merged CSV file, comparing against Json response and adding Piano users IDs to replace customers IDs.

r = requests.get('https://sandbox.tinypass.com/api/v3/publisher/user/search?api_token=zziNT81wShznajW2BD5eLA4VCkmNJ88Guye7Sw4D&aid=o1sRRZSLlw')
x = r.json()
api_df = json_normalize(x, 'users')


dfa = df.set_index('email')
dfa.update(api_df.set_index('email'))
dfa.to_csv("merged_python_corrected.csv")







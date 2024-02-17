import pandas as pd

df = pd.read_csv("item_list.csv")
df = df[~df['Names'].str.contains('combo', case=False)]
df.to_csv("item_list2.csv")
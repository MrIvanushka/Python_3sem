import pandas as pd

df = pd.read_csv("transactions.csv")
m = df[df['STATUS'] == 'OK']
print(m.groupby(by = ['STATUS'])['SUM'].sum())
print(*m.sort_values(by='SUM', ascending=False).iloc[0:3,3])


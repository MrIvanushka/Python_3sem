import pandas as pd

df = pd.read_csv("transactions.csv")
m = df[df['STATUS'] == 'OK']
print("Three max operations: ", end='')
print(*m.sort_values(by='SUM', ascending=False).iloc[0:3,3])
m = m[m['CONTRACTOR'] == 'Umbrella, Inc']
print("Zombie sponsor's operations sum: ", end='')
print(m['SUM'].sum())

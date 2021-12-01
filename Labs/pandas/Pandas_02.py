import pandas as pd
import matplotlib.pyplot as plt


flights = pd.read_csv("flights.csv", index_col=[0])
axs = flights.groupby(by = ['CARGO'])['PRICE','WEIGHT'].sum().plot(kind='bar', rot= 0, subplots= True)
plt.show()
ax = flights['CARGO'].value_counts().plot(kind= 'bar')
plt.show()


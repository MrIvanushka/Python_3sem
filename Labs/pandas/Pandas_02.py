import matplotlib.pyplot as plt
import pandas            as pd


flights = pd.read_csv("flights.csv", index_col=[0])

plt.subplot(1, 3, 1)
flights.groupby(by = ['CARGO'])['PRICE'].sum().plot(kind='bar', rot=0)
plt.title("Полная стоимость")
plt.subplot(1, 3, 2)
flights.groupby(by = ['CARGO'])['WEIGHT'].sum().plot(kind='bar', color='g', rot=0)
plt.title("Вес")
plt.subplot(1, 3, 3)
flights['CARGO'].value_counts().plot(kind= 'bar', color='r', rot=0)
plt.title('Kолличество перелетов')
plt.show()

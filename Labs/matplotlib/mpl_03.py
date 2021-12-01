import matplotlib.pyplot as plt
import pandas as pd

dk = pd.read_csv('students.csv', sep=";", header= None)
dk.columns = ['prep','group', 'marks']
print(dk)
test1 = dk.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
test2 = dk.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
ax = test1.plot(kind='bar', stacked=True, rot= 0)
bx = test2.plot(kind='bar', stacked=True, rot= 0)
plt.show()
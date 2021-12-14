import matplotlib.pyplot as plt
import pandas            as pd

students_info = pd.read_excel('students_info.xlsx')
resultes = pd.read_html('results_ejudge.html')
resultes = resultes[0]
m = students_info.merge(resultes, left_on= 'login',
                       right_on= 'User', how= 'outer')
m.dropna(subset = ['login'], inplace= True)
plt.subplot(1,2,1)
k = m.groupby(by = 'group_faculty')['Solved'].mean()
k.plot.bar(rot= 0, color='red')
plt.subplot(1,2,2)
m.groupby(by = 'group_out')['Score'].mean().plot.bar(rot= 0)
f = m.copy()
z = m.copy()
z.dropna(subset= ['G'], inplace= True)
f.dropna(subset= ['H'], inplace= True)
cool_guys = pd.concat((z,f), axis = 0)
print(cool_guys['group_faculty'].value_counts(),
        '\n------------------------------------\n',
cool_guys['group_out'].value_counts())
plt.show()

import pandas as pd
from matplotlib import pyplot as plt
import os
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\python\\EXTRA')
data = pd.read_csv('salary.csv')
plt.style.use('ggplot')  

ages = data['Age']
all_devs = data['All_Devs']
pyt_salary = data['Python']


plt.xlabel('Ages')
plt.ylabel('Salary')
plt.plot(ages, pyt_salary, color='#f0ad4e', label='Python')

# plt.plot(ages, java_salary,color='#5a5a5a', label='JavaScript')
# plt.plot(ages, all_devs, color='#5cb85c' ,label='JavaScript')

overallmedian = pyt_salary.median()
# print(overallmedian)
# plt.fill_between(ages,pyt_salary,where=(pyt_salary>overallmedian),interpolate=True,color='blue',alpha=0.25)
# plt.fill_between(ages,pyt_salary,where=(pyt_salary<overallmedian),interpolate=True,color='red',alpha=0.25)
plt.fill_between(ages,pyt_salary,all_devs, where=(pyt_salary>all_devs),interpolate=True,color='blue',alpha=0.25)
plt.fill_between(ages,pyt_salary,all_devs, where=(pyt_salary<all_devs),interpolate=True,color='red',alpha=0.25)

plt.legend()
plt.tight_layout()
plt.show()
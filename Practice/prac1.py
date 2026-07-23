import pandas as pd
from matplotlib import pyplot as plt
import os
plt.style.use('ggplot')                                     

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop")
df=pd.read_excel('PJK Monthly Data.xlsx')
print(df.head())
print(df.columns)

parcel=df.loc[:,'Parcel']
date=df.loc[:,'Allot. Dt.']

plt.bar(date,parcel)
plt.xlabel('date')
plt.ylabel('parcels')
plt.tight_layout()
plt.show()

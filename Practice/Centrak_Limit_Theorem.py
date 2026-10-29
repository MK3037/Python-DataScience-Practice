import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('eda_missing_data_dataset1.csv')
Y=df['number_of_strikes']
print(df.describe())
print(df.head())

def ploting(arr):
    plt.hist(arr, bins=30, edgecolor='b')
    plt.xlabel('number of strikes')
    plt.ylabel('frequency')
    plt.show()

ploting(Y)

clt=[]
for i in range(2000):
    sample_mean=Y.sample(n=30,replace=True).mean()
    clt.append(sample_mean)
ploting(clt)
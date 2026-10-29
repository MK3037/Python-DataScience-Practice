import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('eda_missing_data_dataset1.csv')
print(df.describe())
print(df.head())
X=df['number_of_strikes']

print('--Outliers-- ')

print('--IQR Method--')
IQR=X.quantile(0.75)-X.quantile(0.25)
lower_bound=X.quantile(0.25)-(1.5*IQR)
upper_bound=X.quantile(0.75)+(1.5*IQR)
print(df[(X>upper_bound) | (X<lower_bound)])

print('--Zscore Method--')
df['zscore']=(X - X.mean()) / X.std()
print(df.loc[(df['zscore']>3) | (df['zscore']<-3), ['date','number_of_strikes']])

print('--Percentile Method--')
lower_bound=df['number_of_strikes'].quantile(0.01)
upper_bound=df['number_of_strikes'].quantile(0.99)
print(df.loc[(X>upper_bound) | (X<lower_bound), ['date','number_of_strikes']])
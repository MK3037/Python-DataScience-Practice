import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eda_missing_data_dataset1.csv')
Y = df['number_of_strikes']
print(df.head())
n = df.shape[0]

mean_manual = Y.sum() / n
quantile_val = Y.quantile(0.5)
mode_val = Y.mode()

range_val = Y.max() - Y.min()
variance_manual = ((Y - Y.mean()) ** 2 / (n - 1)).sum()
std_val = Y.std()

print('--Central Tendency--')
print(f'Mean:          {Y.mean()}')
print(f'Mean:          {mean_manual}')
print(f'Median:        {Y.median()}')
print(f'Mode:          {mode_val}')
print(f'Quantile(0.5): {quantile_val}')


print('--Statistical Dispersion--')
print(f'Range:             {range_val}')
print(f'Variance:          {Y.var()}')
print(f'Variance:          {variance_manual}')
print(f'Std Deviation:     {std_val}')

print('--Measure of Symmetry and Shape--')
print(f'Skewness:           {Y.skew()}')
print(f'Skewness:           {3*(Y.mean()-Y.median())/Y.std()}')
print(f'Kurtosis:           {Y.kurt()}')
print(f'Kurtosis:           {(Y.quantile(0.75)-Y.quantile(0.25))/(Y.quantile(0.90)-Y.quantile(0.10))}')
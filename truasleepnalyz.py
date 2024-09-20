import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('answr_st.csv')

df = df.rename(columns={'Sleep Hours': 'time_sleep', 'GPA': 'GPA'})

df['GPA'] = df['GPA'].astype(str).str.replace(',', '.').astype(float)
df['time_sleep'] = df['time_sleep'].astype(str).str.replace(',', '.').astype(float)

df = df.dropna(subset=['GPA', 'time_sleep'])

X = df['time_sleep']

X = sm.add_constant(X)

y = df['GPA']

model = sm.OLS(y, X).fit()

beta_value = model.params['time_sleep']
t_value = model.tvalues['time_sleep']
p_value = model.pvalues['time_sleep']

print(f'Beta-value: {beta_value}')
print(f'T-value: {t_value}')
print(f'P-value: {p_value}')

print(model.summary())

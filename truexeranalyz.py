import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('answr_st.csv')

df = df.rename(columns={'Exercise minutes': 'total_exercise_time', 'GPA': 'GPA'})

df['GPA'] = df['GPA'].astype(str).str.replace(',', '.').astype(float)
df['total_exercise_time'] = df['total_exercise_time'].astype(str).str.replace(',', '.').astype(float)

df = df.dropna(subset=['GPA', 'time_sleep'])

X = df['total_exercise_time']

X = sm.add_constant(X)

y = df['GPA']

model = sm.OLS(y, X).fit()

beta_value = model.params['total_exercise_time']
t_value = model.tvalues['total_exercise_time']
p_value = model.pvalues['total_exercise_time']

print(f'Beta-value: {beta_value}')
print(f'T-value: {t_value}')
print(f'P-value: {p_value}')

print(model.summary())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('answr_st.csv')

df = df.rename(columns={'Sleep Hours': 'time_sleep', 'GPA': 'GPA'})

df['GPA'] = df['GPA'].astype(str).str.replace(',', '.').astype(float)
df['time_sleep'] = df['time_sleep'].astype(str).str.replace(',', '.').astype(float)

df = df.dropna(subset=['GPA', 'time_sleep'])

mean_gpa = df.groupby('time_sleep')['GPA'].mean()

std_gpa = df.groupby('time_sleep')['GPA'].std()

plt.figure(figsize=(10, 6))
plt.bar(mean_gpa.index, mean_gpa, yerr=std_gpa, capsize=5, color='skyblue', alpha=0.7)

plt.xlabel('Sleep Time (hours)')
plt.ylabel('GPA')
plt.title('Mean GPA with Error Bars by Sleep Time')

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('answr_st.csv')

df = df.rename(columns={'Exercise Hours': 'exercise_time', 'GPA': 'GPA'})

df['GPA'] = df['GPA'].astype(str).str.replace(',', '.').astype(float)
df['exercise_time'] = df['exercise_time'].astype(str).str.replace(',', '.').astype(float)

df = df.dropna(subset=['GPA', 'exercise_time'])

plt.figure(figsize=(12, 6))
sns.boxplot(x='exercise_time', y='GPA', data=df)

mean_gpa = df.groupby('exercise_time')['GPA'].mean()
std_gpa = df.groupby('exercise_time')['GPA'].std()

plt.errorbar(mean_gpa.index, mean_gpa, yerr=std_gpa, fmt='o', color='red', label='Mean with Std Dev', capsize=5)

plt.title('Boxplot of GPA vs. Exercise Time with Error Bars', fontsize=16)
plt.xlabel('Exercise Time (Hours)', fontsize=12)
plt.ylabel('GPA', fontsize=12)
plt.legend()

plt.show()

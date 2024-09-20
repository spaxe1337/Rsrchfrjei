import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('answr_st.csv')

df_clean = df[['time_sleep', 'GPA']].dropna()

sns.lmplot(x='time_sleep', y='GPA', data=df_clean, aspect=1.5, height=6)

plt.xlabel('Sleep Time (hours)')
plt.ylabel('GPA')
plt.title('GPA vs. Sleep Time with Regression Line')

plt.show()

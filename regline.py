import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('')

df = pd.DataFrame(data)

df['GPA'] = df['GPA'].str.replace(',', '.').astype(float)

sns.lmplot(x='sleep_time', y='GPA', data=df, aspect=1.5, height=6)

plt.xlabel('Sleep Time')
plt.ylabel('GPA')
plt.title('GPA vs. Sleep Time with Regression Line')

plt.show()

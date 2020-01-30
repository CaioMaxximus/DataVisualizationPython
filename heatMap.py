import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (40,30))

data = pd.read_csv('nba.csv', index_col = 'Age')
sns.heatmap(data = data[['Salary']].head(15), annot = True)
plt.show()
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (40,30))

data = pd.read_csv('nba.csv', index_col = 'Age')
dropping_columns = [col for col in data.columns if (col != 'Salary')]
data.drop(dropping_columns, axis = 1, inplace = True)
sns.heatmap(data = data.head(15), annot = True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('nba.csv')

plt.figure(figsize = (20,10))

sns.scatterplot(x = data.Salary , y = data.Age )
plt.show()

sns.scatterplot(x = data.Salary , y = data.Age , hue = data.Position)
plt.show()

sns.regplot(x = data.Salary , y = data.Age)
plt.show()

sns.lmplot(x = 'Salary' , y = 'Age', hue = 'Position', data = data)
plt.show()

sns.swarmplot(x = data['Position'], y = data['Salary'])
plt.show()

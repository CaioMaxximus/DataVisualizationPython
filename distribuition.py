import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data  = pd.read_csv('vgsales-12-4-2019-short.csv')
sns.distplot(a = data['Year'], kde = False, label= "Year")
plt.legend()
plt.show()

sns.kdeplot(data = data['Year'], shade = True) 
plt.show()

sns.jointplot(x = data['Year'], y = data['Critic_Score'], kind = 'kde')
plt.show()
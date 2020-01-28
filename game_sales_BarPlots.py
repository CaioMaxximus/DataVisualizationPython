import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (16,6))
plt.title('Vendas  X  Notas')

data = pd.read_csv('./vgsales-12-4-2019-short.csv') 
sns.barplot(x = 'Rank', y = 'Critic_Score', data = data.head(20))

plt.show()
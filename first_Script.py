import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print('Dead')


data = pd.read_csv('./nba.csv')
print(data.head())
categorical_columns = [col for col in data.columns if(data[col].dtype == 'object' and data[col].index != 'Name')]
print(categorical_columns)
data = data.drop(categorical_columns, axis =1 )
plt.figure(figsize = (16,6))
plt.title('Nba Salarys')
plt.plot(data)
#plt.xdate('')
plt.show()
print(data.head())
# print(categorical_columns)

# print(sns.lineplot(data = data))
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('./nba.csv' , index_col = "Name")
categorical_columns = [col for col in data.columns if(data[col].dtype == 'object')]
data = data.drop(categorical_columns, axis =1 )
plt.figure(figsize = (16,6))
plt.title('Nba Salarys')
sns.lineplot(data)

plt.show()

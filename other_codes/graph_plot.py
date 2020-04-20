import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

data = pd.read_csv('C:\\Users\\Administrator\\Documents\\GitHub\\SNA_project\\complete.csv')
df = pd.DataFrame(data)
df = df[['Name of State / UT', 'Total Confirmed cases']]
states = df['Name of State / UT'].unique()

new_data = pd.DataFrame(columns = df.columns)
for state in states:
	temp = df[(df['Name of State / UT'] == state)]
	new_data = new_data.append(temp[temp['Total Confirmed cases'] == temp['Total Confirmed cases'].max()])
new_data = new_data.drop_duplicates(subset = 'Name of State / UT', keep = 'last')

new_data = new_data.to_csv('bar_plot_data.csv', index=False)

result=pd.read_csv('bar_plot_data.csv')
result.plot(figsize=(15, 5), x='Name of State / UT', y='Total Confirmed cases', kind="bar", color="red")
plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')
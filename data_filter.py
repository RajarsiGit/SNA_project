import pandas as pd
import numpy as np
import pandas as pd
covid_data = pd.read_csv('complete.csv')
df = pd.DataFrame(covid_data)
states = df['Name of State / UT'].unique()
np.savetxt("states.csv", [states], delimiter=',', fmt='%s')
month_names = ['jan_1', 'jan_2', 'feb_1', 'feb_2', 'mar_1', 'mar_2', 'apr_1', 'apr_2']
months = list()
months.append(df[(df['Date'] >= '2020-01-01') & (df['Date'] <= '2020-01-15')])
months.append(df[(df['Date'] >= '2020-01-16') & (df['Date'] <= '2020-01-31')])
months.append(df[(df['Date'] >= '2020-02-01') & (df['Date'] <= '2020-02-15')])
months.append(df[(df['Date'] >= '2020-02-16') & (df['Date'] <= '2020-02-29')])
months.append(df[(df['Date'] >= '2020-03-01') & (df['Date'] <= '2020-03-15')])
months.append(df[(df['Date'] >= '2020-03-16') & (df['Date'] <= '2020-03-31')])
months.append(df[(df['Date'] >= '2020-04-01') & (df['Date'] <= '2020-04-15')])
months.append(df[(df['Date'] >= '2020-04-15') & (df['Date'] <= '2020-04-30')])
statewise = pd.DataFrame(columns = df.columns)
for month, name in zip(months, month_names):
    for state in states:
        temp = month[(month['Name of State / UT'] == state)]
        statewise = statewise.append(temp[temp['Total Confirmed cases'] == temp['Total Confirmed cases'].max()])
    statewise = statewise.drop_duplicates(subset = "Name of State / UT", keep = 'last')
    statewise = statewise[['Name of State / UT', 'Total Confirmed cases']]
    statewise.to_csv(str(str(name) + '_output.csv'), index=False)
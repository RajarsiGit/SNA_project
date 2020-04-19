import pandas as pd
import numpy as np
states = np.genfromtxt('states.csv', delimiter=',', dtype=str)
month_names = ['jan_1', 'jan_2', 'feb_1', 'feb_2', 'mar_1', 'mar_2', 'apr_1', 'apr_2']
month_inputs = list()
for month in month_names:
    temp = pd.read_csv(month + '_output.csv')
    month_inputs.insert(month_names.index(month), temp)
for month in month_names:
    adj = np.zeros((len(states), len(states)), dtype=int)
    arr = np.array(month_inputs[month_names.index(month)]['Name of State / UT'])
    for elem in arr:
        for i in range(len(states)):
            if elem == states[i]:
                j = int(np.where(states == elem)[0])
                for k in range(j+1):
                    adj[k][j] = month_inputs[month_names.index(month)].iloc[j]['Total Confirmed cases']
                    adj[j][k] = month_inputs[month_names.index(month)].iloc[j]['Total Confirmed cases']
                break
    np.savetxt(month + "_adjacency.csv", adj, delimiter=',', fmt='%s')
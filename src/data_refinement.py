import numpy as np
import pandas as pd

def traffic_flow_cleaning():
    df = pd.read_excel('data/raw/traffic-flow-borough-.xls', sheet_name=1)
    df = df.iloc[1:34, :]
    lst = []
    for i in range(1993, 2020):
        temp = df.loc[:, ('LA Code', 'Local Authority', i)]
        year = temp.columns[2]
        temp['year'] = year
        temp['miles'] = temp.iloc[:, 2]
        temp = temp.drop(year, axis=1)
        lst.append(temp)
    full = pd.concat(lst)
    full.to_csv('data/traffic_flow.csv')

if __name__ == '__main__':
    traffic_flow_cleaning()

    test = pd.read_csv('data/traffic_flow.csv')
    print(test)
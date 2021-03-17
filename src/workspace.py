import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('data/traffic-flow-borough-.xls')
    print(df.columns)
    print(df.info())
    print(df.describe())
    print(df.head())
    # print(df['Unnamed: 0'].unique())
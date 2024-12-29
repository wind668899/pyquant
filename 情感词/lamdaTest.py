
import pandas as pd
import numpy as np
from pandas import DataFrame, Series



data = pd.read_csv("data.csv", encoding='UTF-8')
def make_label(df):
    df["sentiment"] = df["star"].apply(lambda x: 1 if x > 3 else 0)


print(data['star'].unique())
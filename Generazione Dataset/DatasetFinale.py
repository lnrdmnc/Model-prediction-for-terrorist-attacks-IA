import numpy as np
import pandas as pd

def creataDataset(year):
    df = pd.read_csv(f"./globalterrorism{year}.csv", encoding="ISO-8859-1")
    db = pd.read_csv(f"{year}.csv")
    merge = pd.merge(left=df, right=db, how='inner', on="Country")
    merge.to_csv(f"terrorism{year}WHR.csv", index=False)
    return merge


dataset2015=creataDataset("2015")
print(dataset2015.columns)
dataset2016=creataDataset("2016")
print(dataset2016.columns)
print(type(dataset2016.columns.to_list()))
dataset2017=creataDataset("2017")
print(dataset2017.columns)
dataset2015.rename(columns={'Region_x':'Region'},inplace=True)
dataset2015.drop('Region_y',axis=1,inplace=True)
dataset2015.drop('Standard Error',axis=1,inplace=True)
dataset2016.rename(columns={'Region_x':'Region'},inplace=True)
dataset2016.drop('Region_y',axis=1,inplace=True)
dataset2016.drop('Lower Confidence Interval',axis=1,inplace=True)
dataset2016.drop('Upper Confidence Interval',axis=1,inplace=True)
dataset2017.drop('Whisker.high' ,axis=1,inplace=True)
dataset2017.drop('Whisker.low',axis=1,inplace=True)
dataset2017.rename(columns={'Happiness.Rank':'Happiness Rank',
       'Happiness.Score':'Happiness Score',
       'Economy..GDP.per.Capita.':'Economy (GDP per Capita)','Health..Life.Expectancy.':'Health (Life Expectancy)',
       'Trust..Government.Corruption.':'Trust (Government Corruption)',
       'Dystopia.Residual':'Dystopia Residual'},inplace=True)
print(np.setdiff1d(dataset2017.columns.values,dataset2016.columns.values))
dataset=pd.concat([dataset2015,dataset2016,dataset2017],names=dataset2015.columns.to_list())
dataset.to_csv("terrorismWHR.csv",index=False)

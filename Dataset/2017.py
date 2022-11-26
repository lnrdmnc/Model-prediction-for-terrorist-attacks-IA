import numpy as np
import pandas as pd
df=pd.read_csv("./dataset/globalterrorismdb_0718dist.csv", encoding="ISO-8859-1")
print(df.head(5))
print(df["related"]!=np.NaN)
df=df[df["iyear"]==2017]
df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)
df=df[['Year','Month','Day','Country','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
print(df.head())
df.to_csv("globalterrorism2017.csv",index=False)
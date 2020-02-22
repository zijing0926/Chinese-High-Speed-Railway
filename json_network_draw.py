# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:28:52 2020

@author: zzhu1
"""

import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

response = requests.get("https://raw.githubusercontent.com/boyan01/ChinaRegionDistrict/master/region.json")
city=json.loads(response.text)
city1=city['districts']
df_province=pd.DataFrame.from_dict(json_normalize(city1), orient='columns')
frame=[]
for i in range(len(city1)):
    df = pd.DataFrame.from_dict(json_normalize(city1[i]['districts']), orient='columns')
    frame.append(df)

all_df=pd.concat(frame)

lis=[all_df,df_province]
coor=pd.concat(lis)

coor=coor.drop(['districts'], axis=1)
coor.columns=['city_cn','level','lon','lat']



coor.to_excel('coor.xlsx',index=None)
#all_df=all_df[all_df['level']=='city']





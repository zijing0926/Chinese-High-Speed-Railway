# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:24:39 2020

@author: zzhu1
"""

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

spillover=pd.read_excel('spillover_network.xlsx')
city_network_iv=pd.read_excel('city_network_iv.xlsx')

cols=['city_cn', 'Population', 'employ1', 'employ2', 'unemployment', 'ind1',
       'ind2', 'ind3', 'ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9', 'ind10',
       'ind11', 'ind12', 'ind13', 'ind14', 'ind15', 'ind16', 'ind17', 'ind18',
       'ind19', 'road', 'water', 'air', 'year',
       'apl', 'node', 'diameter', 'radius', 'average_clustering',
       'transitivity', 'degree', 'betweenness', 'clustering',
       'node_cut', 'center', 'periphery', 'connect', 'city', 'pro_cn', 'pro',
       'region', 'cpi', 'rgdp', 'rgov_exp', 'rwage', 'degree_iv',
       'betweenness_iv', 'clustering_iv', 'node_cut_iv',
       'center_iv', 'periphery_iv', 'connect_iv', 'employment', 'total',
       'skill', 'tourism', 'other_s', 'other_ns', 'lskill', 'ltourism', 'lother_s',
       'lother_ns', 'dom_ind']

city_network_iv=city_network_iv[cols]


city_network_iv['group']='control'
city_network_iv.loc[city_network_iv['connect_iv'] != 0, 'group'] = 'other'
city_network_iv.loc[city_network_iv['connect'] == 1, 'group'] = 'treated'

city_network_iv['control']=0
city_network_iv.loc[city_network_iv['group']=='control','control']=1

city_network_iv['other']=0
city_network_iv.loc[city_network_iv['group']=='other','other']=1

city_network_iv['treated']=0
city_network_iv.loc[city_network_iv['group']=='treated','treated']=1

city_network_iv['has_hsr']=city_network_iv['connect']
city_network_iv['near_hsr']=0
city_network_iv.loc[city_network_iv['connect_iv'] != 0, 'near_hsr'] = 1

df=city_network_iv.merge(spillover,left_on=['city_cn','year'],right_on=['zero','year'],how='left')

columns=['degree',
       'betweenness', 'clustering', 'node_cut',
       'center', 'periphery', 'connect']
for col in columns:
    df[col+'_iv'] = np.where(df['group']=='treated', df[col+'_spill'], df[col+'_iv'])

df=df.drop(columns=['zero','degree_spill','betweenness_spill', 'clustering_spill', 'node_cut_spill', 'center_spill','periphery_spill', 'connect_spill'])
df=df.dropna()

df=df.rename(columns={"degree_iv": "degree_spill", "betweenness_iv": "betweenness_spill","clustering_iv":"clustering_spill","node_cut_iv":"node_cut_spill","center_iv":"center_spill","periphery_iv":"periphery_spill","connect_iv":"connect_spill"})

group2017=df[df['year']==2017]
group2017=group2017[['city_cn','group']]

df=df.merge(group2017,on=['city_cn'],how='left')
df['group_y'].fillna(df.group_x,inplace=True)

      
     

df=df.rename(columns={'group_x':'group','group_y':'group2017'})

df['treated2017']=0
df.loc[df['group2017']=='treated','treated2017']=1

df['other2017']=0
df.loc[df['group2017']=='other','other2017']=1

df['control2017']=0
df.loc[df['group2017']=='control','control2017']=1




df['treat_other']=0
df.loc[df['has_hsr']==1,'treat_other']=1
df.loc[df['near_hsr']==1,'treat_other']=1


      



df.to_excel('spillover_city.xlsx',index=None)



#####
df_before=pd.read_excel('spillover_city.xlsx')

lag_items=['city_cn','Population', 'unemployment','road', 'water', 'air', 'year', 'apl', 'node', 'diameter',
       'radius', 'average_clustering', 'transitivity', 'degree', 'betweenness',
       'clustering', 'node_cut', 'center', 'periphery', 'connect', 'city',
       'pro_cn', 'pro', 'region', 'cpi', 'rgdp', 'rgov_exp', 'rwage',
       'degree_spill', 'betweenness_spill', 'clustering_spill',
       'node_cut_spill', 'center_spill', 'periphery_spill', 'connect_spill',
       'dom_ind', 'group',
       'control', 'other', 'treated', 'group2017', 'treated2017', 'other2017',
       'control2017', 'has_hsr', 'near_hsr']
normal_items=['city_cn', 'total', 'skill', 'tourism', 'other_s', 'other_ns',
       'lskill', 'ltourism', 'lother_s', 'lother_ns', 'employ1', 'employ2','employment','year','ind11','ind13']

df_lag=df_before[lag_items]
df_lag['year']=df_lag['year']+1
df_normal=df_before[normal_items]

df=df_normal.merge(df_lag,on=['city_cn','year'],how='inner')

df.to_excel('spillover_city_lag.xlsx',index=None)

table=df[['degree_spill','degree','betweenness_spill','betweenness','center_spill','center','periphery_spill','periphery']].describe()
table=table.round(2)
table.to_excel('summary_spill.xlsx')

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:07:50 2019

@author: zzhu1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
       'lskill', 'ltourism', 'lother_s', 'lother_ns', 'employ1', 'employ2','employment','year']

df_lag=df_before[lag_items]
df_lag['year']=df_lag['year']+1
df_normal=df_before[normal_items]

df=df_normal.merge(df_lag,on=['city_cn','year'],how='inner')

df1=df[['city_cn','year','lskill','ltourism','lother_s','lother_ns']]
df1.columns=['city_cn','year','skill','tourism','other_s','other_ns']
idx =['city_cn','year']
multi_indexed_df = df1.set_index(idx)
stacked_df = multi_indexed_df .stack(dropna=False)
stacked_df=stacked_df.reset_index()
stacked_df.columns=['city_cn','year','ind_group','ind_employment']
cols=['city_cn', 'Population', 'employ1', 'employ2', 'employment','unemployment','road','air','water','year',
      'degree',
       'betweenness', 'clustering', 'node_cut', 'center', 'periphery',
       'connect','city','pro','region','rgdp','rgov_exp','rwage', 'degree_spill','betweenness_spill', 'clustering_spill', 'node_cut_spill', 'center_spill','periphery_spill', 'connect_spill',
       'dom_ind','group','control','other','treated','group2017','treated2017', 'other2017',
       'control2017', 'has_hsr', 'near_hsr']
df=df[cols]
final=stacked_df.merge(df,on=['city_cn','year'],how='left')
final.to_excel('reshape_spill.xlsx',index=None)
 

###use skill compositions
df=pd.read_excel('spillover_city.xlsx')

df_lag=df_before[lag_items]
df_lag['year']=df_lag['year']+1
df_normal=df_before[normal_items]

df=df_normal.merge(df_lag,on=['city_cn','year'],how='inner')


df1=df[['city_cn','year','skill','tourism','other_s','other_ns']]
#df1.columns=['city_cn','year','skill','tourism','other_s','other_ns']
idx =['city_cn','year']
multi_indexed_df = df1.set_index(idx)
stacked_df = multi_indexed_df .stack(dropna=False)
stacked_df=stacked_df.reset_index()
stacked_df.columns=['city_cn','year','ind_group','ind_employment']
cols=['city_cn', 'Population', 'employ1', 'employ2', 'employment','unemployment','road','air','water','year',
      'degree',
       'betweenness', 'clustering', 'node_cut', 'center', 'periphery',
       'connect','city','pro','region','rgdp','rgov_exp','rwage', 'degree_spill','betweenness_spill', 'clustering_spill', 'node_cut_spill', 'center_spill','periphery_spill', 'connect_spill',
       'dom_ind','group','control','other','treated','group2017','treated2017', 'other2017',
       'control2017', 'has_hsr', 'near_hsr']
df=df[cols]
final=stacked_df.merge(df,on=['city_cn','year'],how='left')
final.to_excel('reshape_spill_compositions.xlsx',index=None)





#############
ind_group=final['ind_group'].unique().tolist()
for ind in ind_group:
    final[ind+'_group']=0
    final.loc[final['ind_group']==ind, ind+'_group']=1
    
years=final['year'].unique().tolist()
for year in years:
    year_str=str(year)
    final['year_'+year_str]=0
    final.loc[final['year']==year,'year_'+year_str]=1

for ind in ind_group:
    for year in years:
        year_str=str(year)
        final[ind+year_str]=final[ind+'_group']*final['year_'+year_str]
final.to_excel('reshape_spill_compositions_fe.xlsx',index=None)

###
import seaborn as sns
sns.set(style="ticks", color_codes=True)
controls = df[['rgdp','rgov_exp','rwage','Population', 'employment','unemployment']]
g = sns.pairplot(controls)
plt.savefig('control_corr.png')
connect=final[['degree','betweenness', 'clustering', 'node_cut', 'center', 'periphery',
       'connect']]
connect_iv=final[['degree_iv',
       'betweenness_iv', 'clustering_iv', 'node_cut_iv', 'center_iv',
       'periphery_iv', 'connect_iv']]

g = sns.pairplot(df,vars=['degree','degree_iv'])
plt.savefig('degree.png')
g = sns.pairplot(df,vars=['betweenness','betweenness_iv'])
plt.savefig('betweenness.png')

g = sns.pairplot(df,vars=['clustering','clustering_iv'])
plt.savefig('clustering.png')
g = sns.pairplot(df,vars=['center','center_iv'])
plt.savefig('center.png')
g = sns.pairplot(df,vars=['periphery','periphery_iv'])
plt.savefig('periphery.png')
g = sns.pairplot(df,vars=['connect','connect_iv'])
plt.savefig('connect.png')
g = sns.pairplot(df,vars=['node_cut','node_cut_iv'])
plt.savefig('node_cut.png')



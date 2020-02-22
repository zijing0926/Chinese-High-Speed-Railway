# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:03:43 2020

@author: zzhu1
"""

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('spillover_city.xlsx')

group2017=df[df['year']==2017]
group2017=group2017[['city_cn','group']]

df=df.merge(group2017,on=['city_cn'],how='left')
df['group_y'].fillna(df.group_x,inplace=True)

df=df.rename(columns={'group_x':'group','group_y':'groupof2017'})




######cities that change groups every year
cols=['rgdp','rgov_exp','employment','Population','skill','tourism','other_ns','other_s']
cols1=['skill','tourism','other_ns','other_s','lskill','ltourism','lother_ns','lother_s']
cols2=['Population','employment','unemployment','rgdp','rgov_exp','rwage','road','air']
cols3=['degree_spill','betweenness_spill','center_spill','periphery_spill']


group=df.groupby(['group','year']).mean()
group=group.reset_index()

groups=group['group'].unique().tolist()



###check for center or periphery cities:
df_center=df.groupby(['center','year']).mean()
df_center=df_center.reset_index()
values=df_center['center'].unique().tolist()

fig=plt.figure(figsize=(12,12))
fig.subplots_adjust(hspace=1, wspace=0.4)
z=1
for c in cols2:
    ax=plt.subplot(5,2,z)
    for v in values:
        center=df_center.copy()
        center=center[center['center']==v]
        center.plot(kind='line',x='year',y=c,ax=ax,label=v,legend=False)
    plt.title('%s'%cols2[z-1])        
    z=z+1    
#fig.suptitle('Comparisons among groups')
handles, labels = ax.get_legend_handles_labels()
#labels=['Eventually Control','Eventually Other','Eventually Treated']
fig.legend(handles, labels, loc='upper center')
plt.savefig('group_center.png')
plt.show() 






fig=plt.figure(figsize=(12,8))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
z=1
for c in cols3:
    ax=plt.subplot(2,2,z)
    for g in groups:
        gro=group.copy()
        gro=gro[gro['group']==g]
        gro.plot(kind='line',x='year',y=c,ax=ax,label=g,legend=False)
    plt.title('%s'%cols3[z-1])        
    z=z+1   
#fig.suptitle('Comparisons among groups')
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center')
plt.savefig('group_comparison.png')
plt.show() 

fig=plt.figure(figsize=(12,12))
fig.subplots_adjust(hspace=1, wspace=0.4)
z=1
for c in cols1:
    ax=plt.subplot(4,2,z)
    for g in groups:
        gro=group.copy()
        gro=gro[gro['group']==g]
        gro.plot(kind='line',x='year',y=c,ax=ax,label=g,legend=False)
    plt.title('%s'%cols1[z-1])        
    z=z+1   
fig.suptitle('Comparisons among groups')
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
plt.savefig('group_comparison1.png')
plt.show() 





##based on the observations on group2017
group_2017=df.groupby(['groupof2017','year']).mean()
group_2017=group_2017.reset_index()


fig=plt.figure(figsize=(12,12))
fig.subplots_adjust(hspace=1, wspace=0.4)
z=1
for c in cols2:
    ax=plt.subplot(5,2,z)
    for g in groups:
        gro=group_2017.copy()
        gro=gro[gro['groupof2017']==g]
        gro.plot(kind='line',x='year',y=c,ax=ax,label=g,legend=False)
        plt.axvline(x=2008,color='r')
    plt.title('%s'%cols2[z-1])        
    z=z+1   
#fig.suptitle('Comparisons among groups')
handles, labels = ax.get_legend_handles_labels()
labels=['Eventually Control','Eventually Other','Eventually Treated']
fig.legend(handles, labels, loc='upper center')
plt.savefig('group_comparison_2017.png')
plt.show() 

####Summary Statistics
##for group 2017
group_2017_ss=df.groupby(['groupof2017'])[cols2].describe().unstack()
#group_2017_ss[cols2] = np.exp(group_2017_ss[cols2])
group_2017_ss=group_2017_ss.reset_index()
group_2017_ss=group_2017_ss[(group_2017_ss['level_1']=='mean')|(group_2017_ss['level_1']=='std')]
g=group_2017_ss.sort_values(by=['level_0','groupof2017'], ascending = False)
g.columns=['variables','catagroy','group','value']

table = pd.pivot_table(g, values='value', index=['variables','catagroy'], columns=['group'])
table=table.round(2)
table.to_excel('summary_statistics.xlsx')
#####for group
group_ss=df.groupby(['group'])[cols2].describe().unstack()
#group_2017_ss[cols2] = np.exp(group_2017_ss[cols2])
group_ss=group_ss.reset_index()
group_ss=group_ss[(group_ss['level_1']=='mean')|(group_ss['level_1']=='std')]
g=group_ss.sort_values(by=['level_0','group'], ascending = False)
g.columns=['variables','catagroy','group','value']

table = pd.pivot_table(g, values='value', index=['variables','catagroy'], columns=['group'])
table=table.round(2)
table.to_excel('summary_statistics_all.xlsx')






####different cols


fig=plt.figure(figsize=(12,12))
fig.subplots_adjust(hspace=1, wspace=0.4)
z=1
for c in cols1:
    ax=plt.subplot(4,2,z)
    for g in groups:
        gro=group_2017.copy()
        gro=gro[gro['group2017']==g]
        gro.plot(kind='line',x='year',y=c,ax=ax,label=g,legend=False)
    plt.title('%s'%cols1[z-1])        
    z=z+1   
fig.suptitle('Comparisons among groups')
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
plt.savefig('group_comparison1_2017.png')
plt.show() 



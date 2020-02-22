# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:30:43 2020

@author: zzhu1
"""

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import geopandas as gpd
import descartes
from shapely.geometry import Point,Polygon
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
import geopy.distance


#import coordinations for all cities
city_sta1=pd.read_excel('coor.xlsx')
city_sta1=city_sta1[~city_sta1['city_cn'].str.contains('省')]
city_sta1=city_sta1[~city_sta1['city_cn'].str.contains('自治区')]
#city_sta1=city_sta1[city_sta1['level']!='province']
additional=pd.read_excel('additional.xlsx')
lis=[city_sta1,additional]
city_sta=pd.concat(lis,sort=False)
city_sta=city_sta.drop_duplicates(subset='city_cn',keep='first')

city_sta['coor']=list(zip(city_sta['lat'],city_sta['lon']))
  
###only for cities at 2003
city=pd.read_excel('proregion.xlsx',sheet_name='pro')
city=city[~city['pro_cn'].str.contains('海南省')]
city.drop(columns=['city','pro_cn'],inplace=True)
city_sta1=city_sta.merge(city,on='city_cn',how='inner')
city_sta1.drop(columns='level',inplace=True)


###calculate distance
import pandas as pd
from scipy.spatial import distance_matrix
from geopy.distance import geodesic
from scipy.spatial.distance import pdist
from geopy.distance import vincenty
import numpy as np
##
##get distance matrix
d=city_sta1[['city_cn','coor']]
lis=d['city_cn'].unique().tolist()
number=d['coor'].values.tolist()
###generate a square
for i in range(len(lis)):
    l=lis[i]
    d[l]=1
    d[l]=d['coor']
    for j in range(len(d[l].unique())):
        d[l][j]=d[l][i] 
        
for l in lis:    
    d[l+'_copy'] = d.apply(lambda x: geodesic(x['coor'], x[l]).kilometers, axis=1)

d=d.set_index('city_cn')
lis_copy=[]
for l in lis:
    lis_copy.append(l+'_copy')
d=d[lis_copy] 
d.columns=d.columns.str.replace('_copy','')    
d.to_excel('dis_json.xlsx')


distance=pd.read_excel('dis_json.xlsx')
distance=distance.set_index('city_cn')
import heapq
#find the five nearest cities' distances for each city here
smallest = distance.apply(lambda x: heapq.nsmallest(6, x), axis=1)
smallest_df = pd.DataFrame(smallest.values.tolist(),index=distance.index)
smallest_df.columns=['Dist_zero','Dist_first','Dist_second','Dist_third','Dist_fourth','Dist_fifth']

#get the id for the five cities for each city
idx = np.argsort(distance.values, 1)[:, 0:6]
name=pd.DataFrame(distance.columns[idx], index=distance.index)
name.columns = ['zero', 'first','second','third','fourth','fifth']
name['year']=2003
frames=[]
frames.append(name)
for year in range(2004,2018):
    names=name.copy()
    names['year']=year
    frames.append(names)
    df1=pd.concat(frames)

#check distance
df=df1.join(smallest_df,how='left')


#df shows the id and distance for all cities

##merge rgdp_2003 for all cities and its ivs
rgdp_2002=pd.read_excel('rgdp_2002.xlsx')
rgdp_2003=pd.read_excel('rgdp_2003.xlsx')
rgdp_2002=rgdp_2002[~rgdp_2002['city_cn'].str.contains('省')]
rgdp_2002=rgdp_2002[~rgdp_2002['city_cn'].str.contains('自治区')]
rgdp_2002=rgdp_2002[rgdp_2002['rgdp']!=0]
rgdp=rgdp_2002.merge(rgdp_2003,on='city_cn',how='outer')
rgdp.rgdp_x.fillna(rgdp.rgdp_y, inplace=True)
del rgdp['rgdp_y']
rgdp.columns=['city_cn','rgdp']
rgdp.to_excel('final_rgdp_2002.xlsx',index=None)
##gdp real
rgdp_2003=pd.read_excel('final_rgdp_2002.xlsx')
rgdp_2003['rgdp']=np.log(rgdp_2003['rgdp'])
df=df.merge(rgdp_2003,left_on='zero',right_on='city_cn',how='left')
df=df.merge(rgdp_2003,left_on='first',right_on='city_cn',how='left')
df.columns=df.columns.str.replace('_x','_zero')
df.columns=df.columns.str.replace('_y','_first')

df=df.merge(rgdp_2003,left_on='second',right_on='city_cn',how='left')
df=df.merge(rgdp_2003,left_on='third',right_on='city_cn',how='left')
df.columns=df.columns.str.replace('_x','_second')
df.columns=df.columns.str.replace('_y','_third')

df=df.merge(rgdp_2003,left_on='fourth',right_on='city_cn',how='left')
df=df.merge(rgdp_2003,left_on='fifth',right_on='city_cn',how='left')
df.columns=df.columns.str.replace('_x','_fourth')
df.columns=df.columns.str.replace('_y','_fifth')

cols = [c for c in df.columns if c[:4] != 'city']
df=df[cols]

gdp=['rgdp_first','rgdp_second','rgdp_third','rgdp_fourth','rgdp_fifth']
df['gdp_total']=df[gdp].sum(axis=1)
dist=['Dist_first','Dist_second','Dist_third','Dist_fourth','Dist_fifth']
df[dist]=np.log(df[dist])
##calculate the share
df['share_first']=(df['rgdp_first']/df['gdp_total'])
df['share_second']=(df['rgdp_second']/df['gdp_total'])*(df['Dist_first']/df['Dist_second'])
df['share_third']=(df['rgdp_third']/df['gdp_total'])*(df['Dist_first']/df['Dist_third'])
df['share_fourth']=(df['rgdp_fourth']/df['gdp_total'])*(df['Dist_first']/df['Dist_fourth'])
df['share_fifth']=(df['rgdp_fifth']/df['gdp_total'])*(df['Dist_first']/df['Dist_fifth'])
share=['share_first','share_second','share_third','share_fourth','share_fifth']
df['share_sum']=df[share].sum(axis=1)
dis_short=df.drop_duplicates(subset='zero',keep='first')
dis_short.to_excel('dis_short_json.xlsx',index=None)



######calculate regular spillover effects for all cities
network=pd.read_excel('networks.xlsx')
network.drop(network.columns[[0]],axis=1,inplace=True)
#network=network.drop(columns=['net_unique'],axis=1)
values = {'net_unique':0, 'apl':0, 'node':0, 'diameter':0, 'radius':0,
       'average_clustering':0, 'transitivity':0, 'degree':0, 'closeness':1,
       'betweenness':0, 'clustering':0, 'node_cut':0, 'center':0, 'periphery':1}

##first
iv=df.merge(network,left_on=['first','year'],right_on=['city','year'],how='left')
iv=iv.fillna(value=values)
iv['connect']=iv.net_unique.apply(lambda x: 0 if x==0 else 1)
iv.rename(columns={'net_unique':'net_unique_first', 'apl':'apl_first', 'node':'node_first', 'diameter':'diameter_first', 'radius':'radius_first',
       'average_clustering':'average_clustering_first', 'transitivity':'transitivity_first', 'degree':'degree_first', 'closeness':'closeness_first',
       'betweenness':'betweenness_first', 'clustering':'clustering_first', 'node_cut':'node_cut_first', 'center':'center_first', 'periphery':'periphery_first','connect':'connect_first'},inplace=True)
iv=iv.drop(columns=['city'],axis=1)


#second
iv=iv.merge(network,left_on=['second','year'],right_on=['city','year'],how='left')
iv=iv.fillna(value=values)
iv['connect']=iv.net_unique.apply(lambda x: 0 if x==0 else 1)
iv.rename(columns={'net_unique':'net_unique_second', 'apl':'apl_second', 'node':'node_second', 'diameter':'diameter_second', 'radius':'radius_second',
       'average_clustering':'average_clustering_second', 'transitivity':'transitivity_second', 'degree':'degree_second', 'closeness':'closeness_second',
       'betweenness':'betweenness_second', 'clustering':'clustering_second', 'node_cut':'node_cut_second', 'center':'center_second', 'periphery':'periphery_second','connect':'connect_second'},inplace=True)
iv=iv.drop(columns=['city'],axis=1)

##third
iv=iv.merge(network,left_on=['third','year'],right_on=['city','year'],how='left')
iv=iv.fillna(value=values)
iv['connect']=iv.net_unique.apply(lambda x: 0 if x==0 else 1)
iv.rename(columns={'net_unique':'net_unique_third', 'apl':'apl_third', 'node':'node_third', 'diameter':'diameter_third', 'radius':'radius_third',
       'average_clustering':'average_clustering_third', 'transitivity':'transitivity_third', 'degree':'degree_third', 'closeness':'closeness_third',
       'betweenness':'betweenness_third', 'clustering':'clustering_third', 'node_cut':'node_cut_third', 'center':'center_third', 'periphery':'periphery_third','connect':'connect_third'},inplace=True)
iv=iv.drop(columns=['city'],axis=1)


##fourth
iv=iv.merge(network,left_on=['fourth','year'],right_on=['city','year'],how='left')
iv=iv.fillna(value=values)
iv['connect']=iv.net_unique.apply(lambda x: 0 if x==0 else 1)
iv.rename(columns={'net_unique':'net_unique_fourth', 'apl':'apl_fourth', 'node':'node_fourth', 'diameter':'diameter_fourth', 'radius':'radius_fourth',
       'average_clustering':'average_clustering_fourth', 'transitivity':'transitivity_fourth', 'degree':'degree_fourth', 'closeness':'closeness_fourth',
       'betweenness':'betweenness_fourth', 'clustering':'clustering_fourth', 'node_cut':'node_cut_fourth', 'center':'center_fourth', 'periphery':'periphery_fourth','connect':'connect_fourth'},inplace=True)
iv=iv.drop(columns=['city'],axis=1)

###fifth
iv=iv.merge(network,left_on=['fifth','year'],right_on=['city','year'],how='left')
iv=iv.fillna(value=values)
iv['connect']=iv.net_unique.apply(lambda x: 0 if x==0 else 1)
iv.rename(columns={'net_unique':'net_unique_fifth', 'apl':'apl_fifth', 'node':'node_fifth', 'diameter':'diameter_fifth', 'radius':'radius_fifth',
       'average_clustering':'average_clustering_fifth', 'transitivity':'transitivity_fifth', 'degree':'degree_fifth', 'closeness':'closeness_fifth',
       'betweenness':'betweenness_fifth', 'clustering':'clustering_fifth', 'node_cut':'node_cut_fifth', 'center':'center_fifth', 'periphery':'periphery_fifth','connect':'connect_fifth'},inplace=True)
iv=iv.drop(columns=['city'],axis=1)


###get iv variables with share*network
iv['apl_iv']=iv['share_first']*iv['apl_first']+iv['share_second']*iv['apl_second']+iv['share_third']*iv['apl_third']+iv['share_fourth']*iv['apl_fourth']+iv['share_fifth']*iv['apl_fifth']
iv['node_iv']=iv['share_first']*iv['node_first']+iv['share_second']*iv['node_second']+iv['share_third']*iv['node_third']+iv['share_fourth']*iv['node_fourth']+iv['share_fifth']*iv['node_fifth']
iv['diameter_iv']=iv['share_first']*iv['diameter_first']+iv['share_second']*iv['diameter_second']+iv['share_third']*iv['diameter_third']+iv['share_fourth']*iv['diameter_fourth']+iv['share_fifth']*iv['diameter_fifth']
iv['radius_iv']=iv['share_first']*iv['radius_first']+iv['share_second']*iv['radius_second']+iv['share_third']*iv['radius_third']+iv['share_fourth']*iv['radius_fourth']+iv['share_fifth']*iv['radius_fifth']
iv['average_clustering_iv']=iv['share_first']*iv['average_clustering_first']+iv['share_second']*iv['average_clustering_second']+iv['share_third']*iv['average_clustering_third']+iv['share_fourth']*iv['average_clustering_fourth']+iv['share_fifth']*iv['average_clustering_fifth']
iv['transitivity_iv']=iv['share_first']*iv['transitivity_first']+iv['share_second']*iv['transitivity_second']+iv['share_third']*iv['transitivity_third']+iv['share_fourth']*iv['transitivity_fourth']+iv['share_fifth']*iv['transitivity_fifth']
iv['degree_iv']=iv['share_first']*iv['degree_first']+iv['share_second']*iv['degree_second']+iv['share_third']*iv['degree_third']+iv['share_fourth']*iv['degree_fourth']+iv['share_fifth']*iv['degree_fifth']
iv['closeness_iv']=iv['share_first']*iv['closeness_first']+iv['share_second']*iv['closeness_second']+iv['share_third']*iv['closeness_third']+iv['share_fourth']*iv['closeness_fourth']+iv['share_fifth']*iv['closeness_fifth']
iv['betweenness_iv']=iv['share_first']*iv['betweenness_first']+iv['share_second']*iv['betweenness_second']+iv['share_third']*iv['betweenness_third']+iv['share_fourth']*iv['betweenness_fourth']+iv['share_fifth']*iv['betweenness_fifth']
iv['clustering_iv']=iv['share_first']*iv['clustering_first']+iv['share_second']*iv['clustering_second']+iv['share_third']*iv['clustering_third']+iv['share_fourth']*iv['clustering_fourth']+iv['share_fifth']*iv['clustering_fifth']
iv['node_cut_iv']=iv['share_first']*iv['node_cut_first']+iv['share_second']*iv['node_cut_second']+iv['share_third']*iv['node_cut_third']+iv['share_fourth']*iv['node_cut_fourth']+iv['share_fifth']*iv['node_cut_fifth']
iv['center_iv']=iv['share_first']*iv['center_first']+iv['share_second']*iv['center_second']+iv['share_third']*iv['center_third']+iv['share_fourth']*iv['center_fourth']+iv['share_fifth']*iv['center_fifth']
iv['periphery_iv']=iv['share_first']*iv['periphery_first']+iv['share_second']*iv['periphery_second']+iv['share_third']*iv['periphery_third']+iv['share_fourth']*iv['periphery_fourth']+iv['share_fifth']*iv['periphery_fifth']
iv['connect_iv']=iv['share_first']*iv['connect_first']+iv['share_second']*iv['connect_second']+iv['share_third']*iv['connect_third']+iv['share_fourth']*iv['connect_fourth']+iv['share_fifth']*iv['connect_fifth']


cols=['zero','year','node_iv','diameter_iv','radius_iv',
      'average_clustering_iv', 'transitivity_iv', 'degree_iv', 'closeness_iv',
       'betweenness_iv', 'clustering_iv', 'node_cut_iv', 'center_iv',
       'periphery_iv', 'connect_iv']

iv_measure=iv[cols]
iv_measure.to_excel('iv_measure.xlsx',index=None)






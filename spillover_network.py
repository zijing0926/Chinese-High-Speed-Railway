 # -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 07:15:33 2020

@author: zzhu1
"""

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import geopandas as gpd
import descartes
from shapely.geometry import Point,Polygon
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

all_dfs = pd.read_excel('network.xlsx', sheet_name=None,header=None,names=['city_from','city_to','net','year'])
fdf = pd.concat(all_dfs, ignore_index=True)
network=fdf.drop_duplicates(keep='first')
city_2018=network[network['year']==2018]
city2018=city_2018['city_from'].append(city_2018['city_to'])
city2018=city2018.drop_duplicates(keep='first')
city_list=city2018.tolist()
#citydict = {city : pd.DataFrame() for city in city_list[0:2]}
#for key,value in citydict.items():
    #citydict[key] = df[:][df.city== key]
data=[]
for city in city_list:
    #print(city)
    network_copy=network.copy()
    network_copy = network_copy[network_copy.city_from != city]
    network_copy = network_copy[network_copy.city_to != city]

    G=[nx.from_pandas_edgelist(network_copy[network_copy['year']==i], 'city_from', 'city_to') for i in range(2008,2019)]
    frames=[]
    i=1
    year=2007
    for graph in G:
        year=year+1
        for g in nx.connected_component_subgraphs(graph):
            #print(g)
            df = pd.DataFrame(g.nodes,columns=['city'])
        #g.neighbors(g.nodes)
        #for a whole network
            df['net_unique']=i
            i=i+1
           #df['apl']=nx.average_shortest_path_length(g)
           #df['node']=len(g)
           #df['diameter']=nx.diameter(g)
           #df['radius']=nx.radius(g)
           #df['average_clustering']=nx.average_clustering(g)
           #df['transitivity']=nx.transitivity(g)
        #individual
        #df['neighbors']=g.neighbors(df.city)
            df['degree'] = dict(g.degree(g.nodes())).values()
        #closeCent=nx.closeness_centrality(g)
        #df['closeness']=closeCent.values()
            btwnCent=nx.betweenness_centrality(g)
            df['betweenness']=btwnCent.values()
            clustering=nx.clustering(g)
            df['clustering']=clustering.values()
            node_cut=nx.minimum_node_cut(g)
            df['node_cut']=df.city.apply(lambda x: 1 if x in node_cut else 0)
            center=nx.center(g)
            df['center']=df.city.apply(lambda x: 1 if x in center else 0)
            periphery=nx.periphery(g)
            df['periphery']=df.city.apply(lambda x: 1 if x in periphery else 0)
            df['year']=year
        
        
        #df['clustering']=nx.clustering(g)
        #sets.append(nx.minimum_node_cut(g,g.nodes()))
            frames.append(df)
            df_city=pd.concat(frames)
    data.append(df_city)


      
    #print(len(apl))
dic=dict(zip(city_list,data))

variables=pd.read_excel('variables.xlsx')

variables=variables[~variables['city_cn'].str.contains('省')]
variables=variables[~variables['city_cn'].str.contains('自治区')]

variables=variables[['city_cn','year']]
data1=[]
for key,value in dic.items():
    #print(value)
    city_network=variables.merge(value,left_on=['city_cn','year'],right_on=['city','year'],how='left')
    values = {'net_unique':0, 'degree':0, 
       'betweenness':0, 'clustering':0, 'node_cut':0, 'center':0, 'periphery':1}
    city_network=city_network.fillna(value=values)
    city_network['connect']=city_network.net_unique.apply(lambda x: 0 if x==0 else 1)
    city_network.drop(columns=['city'],inplace=True)
    city_network['city']=key
    data1.append(city_network)
    
dic1=dict(zip(city_list,data1))

all_cities=pd.concat(data1)


 
dis=pd.read_excel('dis_short_json.xlsx')
dis=dis[['zero','first','second','third','fourth','fifth','share_first','share_second','share_third','share_fourth','share_fifth']]

total=dis.merge(all_cities,left_on=['zero','first'],right_on=['city','city_cn'],how='outer')
total=total.dropna()
total1=total.merge(all_cities,left_on=['zero','second','year'],right_on=['city','city_cn','year'],how='left')
total1=total1.drop(columns=['city_cn_x','city_x','city_cn_y','city_y'])
total1.columns=total1.columns.str.replace('_x','_first')
total1.columns=total1.columns.str.replace('_y','_second')

##third and fourth
total2=total1.merge(all_cities,left_on=['zero','third','year'],right_on=['city','city_cn','year'],how='left')
total3=total2.merge(all_cities,left_on=['zero','fourth','year'],right_on=['city','city_cn','year'],how='left')
total3=total3.drop(columns=['city_cn_x','city_x','city_cn_y','city_y'])
total3.columns=total3.columns.str.replace('_x','_third')
total3.columns=total3.columns.str.replace('_y','_fourth')
#fifth
total4=total3.merge(all_cities,left_on=['zero','fifth','year'],right_on=['city','city_cn','year'],how='left')
total4=total4.drop(columns=['city_cn','city'])
iv=total4

iv['degree_spill']=iv['share_first']*iv['degree_first']+iv['share_second']*iv['degree_second']+iv['share_third']*iv['degree_third']+iv['share_fourth']*iv['degree_fourth']+iv['share_fifth']*iv['degree']
#iv['closeness_iv']=iv['share_first']*iv['closeness_first']+iv['share_second']*iv['closeness_second']+iv['share_third']*iv['closeness_third']+iv['share_fourth']*iv['closeness_fourth']+iv['share_fifth']*iv['closeness']
iv['betweenness_spill']=iv['share_first']*iv['betweenness_first']+iv['share_second']*iv['betweenness_second']+iv['share_third']*iv['betweenness_third']+iv['share_fourth']*iv['betweenness_fourth']+iv['share_fifth']*iv['betweenness']
iv['clustering_spill']=iv['share_first']*iv['clustering_first']+iv['share_second']*iv['clustering_second']+iv['share_third']*iv['clustering_third']+iv['share_fourth']*iv['clustering_fourth']+iv['share_fifth']*iv['clustering']
iv['node_cut_spill']=iv['share_first']*iv['node_cut_first']+iv['share_second']*iv['node_cut_second']+iv['share_third']*iv['node_cut_third']+iv['share_fourth']*iv['node_cut_fourth']+iv['share_fifth']*iv['node_cut']
iv['center_spill']=iv['share_first']*iv['center_first']+iv['share_second']*iv['center_second']+iv['share_third']*iv['center_third']+iv['share_fourth']*iv['center_fourth']+iv['share_fifth']*iv['center']
iv['periphery_spill']=iv['share_first']*iv['periphery_first']+iv['share_second']*iv['periphery_second']+iv['share_third']*iv['periphery_third']+iv['share_fourth']*iv['periphery_fourth']+iv['share_fifth']*iv['periphery']
iv['connect_spill']=iv['share_first']*iv['connect_first']+iv['share_second']*iv['connect_second']+iv['share_third']*iv['connect_third']+iv['share_fourth']*iv['connect_fourth']+iv['share_fifth']*iv['connect']

cols=['zero','year','degree_spill',
       'betweenness_spill', 'clustering_spill', 'node_cut_spill', 'center_spill',
       'periphery_spill', 'connect_spill']
iv=iv[cols]

iv.to_excel('spillover_network.xlsx',index=None)
    
    
    
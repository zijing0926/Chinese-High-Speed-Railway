# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:44:56 2019

@author: zzhu1
"""

import pandas as pd
import numpy as np
#network variables
network=pd.read_excel('networks.xlsx')
network.drop(network.columns[[0]],axis=1,inplace=True)
network.rename(columns={network.columns[0]:'city_cn'},inplace=True)
#other variables
variables=pd.read_excel('variables.xlsx')
#get rid of the provinces
variables=variables[~variables['city_cn'].str.contains('省')]
variables=variables[~variables['city_cn'].str.contains('自治区')]
variables=variables[~variables['city_cn'].str.contains('海口市')]
variables=variables[~variables['city_cn'].str.contains('三亚市')]


#merge on raw dataset and fillnas

city_network=variables.merge(network,on=['city_cn','year'],how='left')
values = {'net_unique':0, 'apl':0, 'node':0, 'diameter':0, 'radius':0,
       'average_clustering':0, 'transitivity':0, 'degree':0, 'closeness':1,
       'betweenness':0, 'clustering':0, 'node_cut':0, 'center':0, 'periphery':1}
city_network=city_network.fillna(value=values)
city_network['connect']=city_network.net_unique.apply(lambda x: 0 if x==0 else 1)


#add province, add region
pro=pd.read_excel('proregion.xlsx',sheet_name='pro')
region=pd.read_excel('proregion.xlsx',sheet_name='region')
city_network=city_network.merge(pro,on='city_cn',how='left')
city_network=city_network.merge(region,on='pro_cn',how='left')

###delete nans
city_network=city_network.dropna(subset=['ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','city'])
cpi=pd.read_excel('cpi.xls',sheet_name='Sheet1')
city_network=city_network.merge(cpi,on='year',how='left')
real_terms=['gdp','gov_exp','wage']
city_network['rgdp']=(city_network['gdp']/city_network['cpi'])*100
city_network['rgov_exp']=(city_network['gov_exp']/city_network['cpi'])*100
city_network['rwage']=(city_network['wage']/city_network['cpi'])*100

rgdp_2003=city_network[city_network['year']==2003][['city_cn','rgdp']]
rgdp_2003.to_excel('rgdp_2003.xlsx',index=None)

network_measure=['city_cn','year','apl', 'node', 'diameter',
       'radius', 'average_clustering', 'transitivity', 'degree', 'closeness',
       'betweenness', 'clustering', 'node_cut', 'center', 'periphery',
       'connect']
network_mea=city_network[network_measure]
network_mea.to_excel('network_mea.xlsx',index=None)
##add iv
iv_measure=pd.read_excel('iv_measure.xlsx')
city_network_iv=city_network.merge(iv_measure,left_on=['city_cn','year'],right_on=['zero','year'],how='left')
city_network_iv=city_network_iv.dropna(subset=['node_iv','diameter_iv','radius_iv',
      'average_clustering_iv', 'transitivity_iv', 'degree_iv', 'closeness_iv',
       'betweenness_iv', 'clustering_iv', 'node_cut_iv', 'center_iv',
       'periphery_iv', 'connect_iv'])




###transfer datasets
city_network_iv['employment']=city_network_iv['employ1']+city_network_iv['employ2']
city_network_iv['air'] = pd.to_numeric(city_network_iv.air,errors='coerce')
logcolumns=['Population',  'employment', 'employ1','employ2','ind1', 'ind10', 'ind11', 'ind12',
       'ind13', 'ind14', 'ind15', 'ind16', 'ind17', 'ind18', 'ind19', 'ind2',
       'ind3', 'ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9','rgdp', 'rgov_exp', 
       'rwage', 'unemployment','road','air','water']#,
city_network_iv[logcolumns]=city_network_iv[logcolumns]*10000
fna=['road','air','water']
industries=['ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19']
skill=['ind7','ind10','ind11','ind12','ind13','ind18']
tourism=['ind9']
other_s=['ind6','ind8','ind14','ind15','ind16','ind17','ind19']
other_ns=['ind1','ind2','ind3','ind4','ind5']
city_network_iv['total']=city_network_iv[industries].sum(axis=1)
city_network_iv['skill']=(city_network_iv[skill].sum(axis=1)/city_network_iv['total'])*100
city_network_iv['tourism']=(city_network_iv[tourism].sum(axis=1)/city_network_iv['total'])*100
city_network_iv['other_s']=(city_network_iv[other_s].sum(axis=1)/city_network_iv['total'])*100
city_network_iv['other_ns']=(city_network_iv[other_ns].sum(axis=1)/city_network_iv['total'])*100

city_network_iv['skill_d']=city_network_iv[skill].idxmax(axis=1)
city_network_iv['tourism_d']=city_network_iv[tourism].idxmax(axis=1)
city_network_iv['other_s_d']=city_network_iv[other_s].idxmax(axis=1)
city_network_iv['other_ns_d']=city_network_iv[other_ns].idxmax(axis=1)
##just the level of employment in each group
city_network_iv['lskill']=city_network_iv[skill].sum(axis=1)
city_network_iv['ltourism']=city_network_iv[tourism].sum(axis=1)
city_network_iv['lother_s']=city_network_iv[other_s].sum(axis=1)
city_network_iv['lother_ns']=city_network_iv[other_ns].sum(axis=1)


copy=city_network_iv.copy()
keep=['city_cn','year','skill','tourism','other_s','other_ns']
copy=copy[keep]
city_year=[copy[copy['year']==i] for i in range(2003,2018)]
frames=[]
for i in range(15):
    #generate rank across the country
    city_year[i]['skill_rank']=city_year[i]['skill'].rank()
    city_year[i]['tourism_rank']=city_year[i]['tourism'].rank()
    city_year[i]['others_rank']=city_year[i]['other_s'].rank()
    city_year[i]['otherns_rank']=city_year[i]['other_ns'].rank()
    city_year[i]['dom_ind']=city_year[i][['skill_rank','tourism_rank','others_rank','otherns_rank']].idxmin(axis=1)
    frames.append(city_year[i])
frame=pd.concat(frames)
keep=['city_cn','year','dom_ind']
frame=frame[keep]
city_network_iv=city_network_iv.merge(frame,on=['city_cn','year'],how='left')

city_network_iv[fna]=city_network_iv[fna].fillna(value=0)
city_network_iv[fna]=city_network_iv[fna].transform(lambda x: x+1)


city_network_iv=city_network_iv[(city_network_iv[['Population', 'employment',  'employ1','employ2','ind1', 'ind10', 'ind11', 'ind12',
       'ind13', 'ind14', 'ind15', 'ind16', 'ind17', 'ind18', 'ind19', 'ind2',
       'ind3', 'ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9','rgdp', 'rgov_exp', 'rwage', 'unemployment']] >0).all(axis=1)]
city_network_iv=city_network_iv.drop(columns=['total_ride','rail','net_unique','zero'],axis=1)


cols=['Population', 'employ1', 'employ2', 'unemployment', 'ind1',
       'ind2', 'ind3', 'ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9', 'ind10',
       'ind11', 'ind12', 'ind13', 'ind14', 'ind15', 'ind16', 'ind17', 'ind18',
       'ind19', 'gdp', 'gov_exp', 'wage', 'road', 'water', 'air',
       'apl', 'node', 'diameter', 'radius', 'average_clustering',
       'transitivity', 'degree', 'closeness', 'betweenness', 'clustering',
       'node_cut', 'center', 'periphery', 'connect',  'rgdp', 'rgov_exp', 'rwage', 'node_iv', 'diameter_iv',
       'radius_iv', 'average_clustering_iv', 'transitivity_iv', 'degree_iv',
       'closeness_iv', 'betweenness_iv', 'clustering_iv', 'node_cut_iv',
       'center_iv', 'periphery_iv', 'connect_iv', 'employment', 'total',
       'skill', 'tourism', 'other_s', 'other_ns']
city_network_iv=city_network_iv.sort_values(by=['city_cn','year'])

###still need to check how to calculate growth rate
#for c in cols:
 #   city_network_iv[c] = city_network_iv[c].replace(r'\s+', np.nan, regex=True)
  #  city_network_iv[c] = city_network_iv[c].fillna(0)
   # city_network_iv[c]=city_network_iv[c].transform(lambda x: x+1)
    #city_network_iv[c]=np.log(city_network_iv[c])
    #city_network_iv[c+'_lag']=city_network_iv[c].shift(1)
    #city_network_iv['gr_'+c]=((city_network_iv[c]-city_network_iv[c+'_lag'])/city_network_iv[c+'_lag'])*100
    #city_network_iv['gr_'+c]=city_network_iv[c]-city_network_iv[c+'_lag']
    #city_network_iv=city_network_iv[city_network_iv['year']!=2003]
logcolumns=logcolumns+['lskill','ltourism', 'lother_s', 'lother_ns']
city_network_iv[logcolumns] = np.log(city_network_iv[logcolumns])


##add neighbor
nei=pd.read_excel('nei.xlsx')
nei=nei.drop(columns=['employment'],axis=1)
city_network_iv=city_network_iv.merge(nei,on=['city_cn','year'],how='left')      

diff={'skill_diff':5,'tourism_diff':5,'other_s_diff':5,'other_ns_diff':5}
city_network_iv=city_network_iv.fillna(value=diff)

intersection=['degree', 'closeness',
       'betweenness', 'clustering', 'node_cut', 'center', 'periphery',
       'connect','degree_iv','closeness_iv', 'betweenness_iv', 'clustering_iv', 'node_cut_iv','center_iv', 'periphery_iv', 'connect_iv']
for variable in intersection:
    city_network_iv['skill_'+variable]=city_network_iv[variable]*city_network_iv['skill_diff']
    city_network_iv['tourism_'+variable]=city_network_iv[variable]*city_network_iv['tourism_diff']
    city_network_iv['other_s_'+variable]=city_network_iv[variable]*city_network_iv['other_s_diff']
    city_network_iv['other_ns_'+variable]=city_network_iv[variable]*city_network_iv['other_ns_diff']





city_network_iv.to_excel('city_network_iv.xlsx',index=None)



##calculate percentage change by city,year group
#c=cnetwork_iv.groupby(['city_cn', 'year']).pct_change()
#cnetwork_iv.assign(pct_change=cnetwork_iv.groupby(['city_cn', 'year']).employ1.pct_change())

#date_range=pd.period_range('2003','2017',freq='y')

#cnetwork[['YC','SC']]=city_network_iv.sort_values(['year']).groupby('city')[['employ1','employ2']].pct_change()


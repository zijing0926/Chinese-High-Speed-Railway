# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:33:13 2019

@author: zzhu1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dis=pd.read_excel('dis_short_json.xlsx')
dis=dis.drop(columns=['year','Dist_zero','rgdp_first','rgdp_second','rgdp_third','rgdp_fourth','rgdp_fifth','gdp_total','rgdp_zero'],axis=1)
dist=['Dist_first','Dist_second','Dist_third','Dist_fourth','Dist_fifth']
dis[dist]=np.exp(dis[dist])



 
#with open('distance_sum.tex','w') as tf:
#    tf.write(dis.describe().to_latex())
     #tf.write(dis.describe().to_latex().replace('\n', '\n\\caption{Summary Statistics}\\\n', 1))

dis=dis.sort_values('Dist_first')
#draw distributions of distances for first to fifth nearest cities

cols=['Dist_first', 'Dist_second', 'Dist_third', 'Dist_fourth','Dist_fifth']
dis['total']=dis[cols].sum(axis=1)
dis['aver_distance']=dis[cols].mean(axis=1)
distance_sum=dis[['Dist_first','Dist_second','Dist_third','Dist_fourth','Dist_fifth','total','aver_distance']].describe(percentiles=[0.25,0.5,0.75,0.99])
distance_sum.loc['count'] = distance_sum.loc['count'].astype(int).astype(str)
distance_sum.iloc[1:] = distance_sum.iloc[1:].applymap('{:.2f}'.format)
distance_sum.to_excel('distance_sum.xlsx')
distance_sum.to_latex('distance_sum.tex')

#plot distance distribution
fig, axes = plt.subplots(1, 5, figsize=(8,2.5), dpi=100, sharex=True, sharey=True)
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:pink', 'tab:olive']
for i, (ax, col) in enumerate(zip(axes.flatten(), cols)):
    x = dis[col]
    ax.hist(x, alpha=0.8, bins=50, density=True, stacked=True, label=str(col), color=colors[i])
    ax.set_title(col)
    perc=np.percentile(x, 99)
    ax.axvline(x=perc, color='black', linestyle='dashed', linewidth=1)
    ax.text(perc*1.1,0.0125*0.9, '{:.2f}'.format(perc))
    ax.text(perc*1.1,0.0125*0.98, '99%:')


#plt.suptitle('Probability Histogram of Distance(km) in Order', y=1, size=10)
#ax.set_xlim(50, 70); ax.set_ylim(0, 1);
plt.tight_layout()
plt.savefig('Distance Distribution.png')

#plot distribution plot with fit curve in the same graph
import seaborn as sns
sns.set_style("white")

kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
plt.figure(figsize=(12,12))#, dpi= 80)
for i in range(len(cols)):
    col=cols[i]
    x=dis[col]
    perc=np.percentile(x, 99)
    ax=sns.distplot(x, color=colors[i], label=cols[i], **kwargs)
    ax.axvline(x=perc, color='black', linestyle='dashed', linewidth=2)
    ax.text(perc*1.01,0.013, '%d'%perc)
plt.xlabel('Distance(km)')
plt.legend()
plt.tight_layout()
plt.savefig('Distance_combine.png')



#scatter plot, maynot be necessary
dis.reset_index(inplace=True)
ax=plt.gca()
dis.plot(kind='scatter', x='index', y='Dist_first',ax=ax)
dis.plot(kind='scatter', x='index', y='Dist_second',ax=ax,c='red')


##add province and region information
pro=pd.read_excel('proregion.xlsx',sheet_name='pro')
region=pd.read_excel('proregion.xlsx',sheet_name='region')
pro_region=pro.merge(region,on='pro_cn',how='left')
pro_region=pro_region.drop(columns=['city','pro_cn'],axis=1)

##add provinces information
cols=['zero','first','second','third','fourth','fifth']
for col in cols:
    dis=dis.merge(pro_region,left_on=col,right_on='city_cn',how='left')
    dis=dis.drop(columns=['city_cn'],axis=1)
    dis=dis.rename(columns={'pro':'pro_'+col, 'region': 'region_'+col})
cols=['first','second','third','fourth','fifth']
lis_pro=[]
lis_re=[]
for col in cols:
    dis['same_pro_'+col] = dis['pro_zero'] == dis['pro_'+col]
    dis['same_pro_'+col]=dis['same_pro_'+col]*1
    lis_pro.append('same_pro_'+col)
    dis['same_re_'+col] = dis['region_zero'] == dis['region_'+col]
    dis['same_re_'+col]=dis['same_re_'+col]*1
    lis_re.append('same_re_'+col)
    
##describe the data
count=[]
for col in lis_pro:
    my_tab = pd.crosstab(index=dis[col],  # Make a crosstab
                         columns=col,
                         margins=True)      # Name the count column
    count.append(my_tab)
freq=pd.concat(count,axis=1)
freq=freq.drop(columns=['All'],axis=1)
freq_ratio=freq/freq.loc["All"]
freq_ratio.columns=['first','second','third','fourth','fifth']

##add region information


count=[]
for col in lis_re:
    my_tab = pd.crosstab(index=dis[col],  # Make a crosstab
                         columns=col,
                         margins=True)      # Name the count column
    count.append(my_tab)
freq_re=pd.concat(count,axis=1)
freq_re=freq_re.drop(columns=['All'],axis=1)
freq_ratio_re=freq_re/freq_re.loc["All"]
freq_ratio_re.columns=['first','second','third','fourth','fifth']
frames=[freq_ratio,freq_ratio_re]
freqs=pd.concat(frames)
freqs=freqs.iloc[[1,4],:]
ax = freqs.T.plot(kind='bar', title ="Ratio of Sharing Same Province/Region", figsize=(15, 10), legend=True, fontsize=12)
ax.legend(["Same Province", "Same Region"])
plt.savefig('share_same.png')


#x=np.linspace(1,500,200)
#y=np.log(1+10/x)/10
#z=1/np.log(x)
#plt.plot(x,y)
#plt.plot(x,z)

###plot shares
cols=['share_first','share_second','share_third','share_fourth','share_fifth','share_sum']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:pink', 'tab:olive','tab:purple']
fig, axes = plt.subplots(2, 3, figsize=(8,2.5), dpi=100, sharex=True, sharey=True)
for i, (ax, col) in enumerate(zip(axes.flatten(), cols)):
    x = dis[col]
    ax.hist(x, bins=10,density=True, stacked=True, label=str(col), color=colors[i])
    ax.set_title(col)

#plt.suptitle('Probability Histogram of Distance(km) in Order', y=1, size=10)
#ax.set_xlim(50, 70); ax.set_ylim(0, 1);
plt.tight_layout()
plt.savefig('share_dist.png')
#plt.savefig('Distance Distribution.png')



















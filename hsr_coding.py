# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:10:03 2019

@author: zzhu1
"""
#import packages
import pandas as pd
import numpy as np
#reset: reset the variable explorer
#clear:clear console
##combine yearly data with industries employment
########year 2003
#sheet1
year2003=pd.read_excel('2004.xls', sheet_name='1',usecols='B,D,J,L,N,AB,AD,AF,AH,AJ,AL,AN,AP,AR,AT,AV,AX,AZ,BB,BD,BF,BH,BJ,BL,BW')
column_names=year2003.iloc[0]
year2003=year2003[4:]
year2003.columns=column_names.index
year2003.rename(columns={year2003.columns[0]:'city_cn'},inplace=True)

#year2003=year2003.dropna()
#sheet2
year2003_1=pd.read_excel('2004.xls', sheet_name='2',usecols='B,BB,BW')
column_names_1=year2003_1.iloc[0]
year2003_1=year2003_1[4:]
year2003_1.columns=column_names_1.index
year2003_1.rename(columns={year2003_1.columns[0]:'city_cn'},inplace=True)

#year2003_1=year2003_1.dropna()
#sheet 3
year2003_2=pd.read_excel('2004.xls', sheet_name='3',usecols='B,Q,R,S,T,U')
column_names_2=year2003_2.iloc[0]
year2003_2=year2003_2[4:]
year2003_2.columns=column_names_2.index
year2003_2.rename(columns={year2003_2.columns[0]:'city_cn'},inplace=True)
#year2003_2=year2003_2.dropna()
#merge dfs
year_2003=year2003.merge(year2003_1.merge(year2003_2,on='city_cn',how='inner'),on='city_cn',how='inner')
year_2003['year']=2003
year_2003.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','wage','total_ride','rail','road','water','air','year']
#unit=['employ1','unemployment','air','wage']
#year_2003[unit]=year_2003[unit]/10000

########year 2004
#sheet1
year2004=pd.read_excel('2005.xls', sheet_name='1',usecols='B,D,J,L,N,AB,AD,AF,AH,AJ,AL,AN,AP,AR,AT,AV,AX,AZ,BB,BD,BF,BH,BJ,BL,BW')
column_names=year2004.iloc[0]
year2004=year2004[4:]
year2004.columns=column_names.index
year2004.rename(columns={year2004.columns[0]:'city_cn'},inplace=True)

#year2003=year2003.dropna()
#sheet2
year2004_1=pd.read_excel('2005.xls', sheet_name='2',usecols='B,AZ,BU')
column_names_1=year2004_1.iloc[0]
year2004_1=year2004_1[4:]
year2004_1.columns=column_names_1.index
year2004_1.rename(columns={year2004_1.columns[0]:'city_cn'},inplace=True)

#year2003_1=year2003_1.dropna()
#sheet 3
year2004_2=pd.read_excel('2005.xls', sheet_name='3',usecols='B,Q,R,S,T,U')
column_names_2=year2004_2.iloc[0]
year2004_2=year2004_2[4:]
year2004_2.columns=column_names_2.index
year2004_2.rename(columns={year2004_2.columns[0]:'city_cn'},inplace=True)
#year2003_2=year2003_2.dropna()
#merge dfs
year_2004=year2004.merge(year2004_1.merge(year2004_2,on='city_cn',how='inner'),on='city_cn',how='inner')
year_2004['year']=2004
year_2004.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','wage','total_ride','rail','road','water','air','year']
#unit=['employ1','unemployment','air','wage']
#year_2004[unit]=year_2004[unit]/10000

########year 2005
#sheet2-1
year2005=pd.read_excel('2006.xls', sheet_name='2－1',usecols='A,C,I,K,M,U,W,Y')
column_names=year2005.iloc[3]
year2005=year2005[7:]
year2005.columns=column_names
year2005.rename(columns={year2005.columns[0]:'city_cn'},inplace=True)
##2-6
year2005_1=pd.read_excel('2006.xls', sheet_name='2-6',usecols='B,D,F,H')
column_names=year2005_1.iloc[3]
year2005_1=year2005_1[6:]
year2005_1.columns=column_names
year2005_1.rename(columns={year2005_1.columns[0]:'city_cn'},inplace=True)
##2-7
year2005_2=pd.read_excel('2006.xls', sheet_name='2-7',usecols='B,D,F,H')
column_names=year2005_2.iloc[4]
year2005_2=year2005_2[7:]
year2005_2.columns=column_names
year2005_2.rename(columns={year2005_2.columns[0]:'city_cn'},inplace=True)
##2-8
year2005_3=pd.read_excel('2006.xls', sheet_name='2-8',usecols='B,D,F,H')
column_names=year2005_3.iloc[4]
year2005_3=year2005_3[7:]
year2005_3.columns=column_names
year2005_3.rename(columns={year2005_3.columns[0]:'city_cn'},inplace=True)
##2-9
year2005_4=pd.read_excel('2006.xls', sheet_name='2-9',usecols='B,D,F,H')
column_names=year2005_4.iloc[4]
year2005_4=year2005_4[7:]
year2005_4.columns=column_names
year2005_4.rename(columns={year2005_4.columns[0]:'city_cn'},inplace=True)
##2-10
year2005_5=pd.read_excel('2006.xls', sheet_name='2-10',usecols='B,D,F,H,J')
column_names=year2005_5.iloc[4]
year2005_5=year2005_5[7:]
year2005_5.columns=column_names
year2005_5.rename(columns={year2005_5.columns[0]:'city_cn'},inplace=True)
##gdp
year2005_6=pd.read_excel('2006.xls', sheet_name='2-13',usecols='B,D')
column_names=year2005_6.iloc[4]
year2005_6=year2005_6[7:]
year2005_6.columns=column_names
year2005_6.rename(columns={year2005_6.columns[0]:'city_cn'},inplace=True)
##gov_exp
year2005_7=pd.read_excel('2006.xls', sheet_name='2-25',usecols='B,E')
column_names=year2005_7.iloc[4]
year2005_7=year2005_7[7:]
year2005_7.columns=column_names
year2005_7.rename(columns={year2005_7.columns[0]:'city_cn'},inplace=True)
##wage
year2005_8=pd.read_excel('2006.xls', sheet_name='2-28',usecols='B,H')
column_names=year2005_8.iloc[3]
year2005_8=year2005_8[6:]
year2005_8.columns=column_names
year2005_8.rename(columns={year2005_8.columns[0]:'city_cn'},inplace=True)
#ridership
year2005_9=pd.read_excel('2006.xls', sheet_name='2-34',usecols='B,D,E,F,G,H')
column_names=year2005_9.iloc[4]
year2005_9=year2005_9[6:]
year2005_9.columns=column_names
year2005_9.rename(columns={year2005_9.columns[0]:'city_cn'},inplace=True)
####combine for year 2015
year_2005=year2005.merge(year2005_1.merge(year2005_2.merge(year2005_3.merge(year2005_4.merge(year2005_5.merge(year2005_6.merge(year2005_7.merge(year2005_8.merge(year2005_9,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2005['year']=2005
year_2005.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','wage','total_ride','rail','road','water','air','year']
#unit=['employ1','unemployment','air','wage']
#year_2005[unit]=year_2005[unit]/10000



####year 2006
##for industry employments
year2006=pd.read_excel('2007.xls',usecols='A,H,J,L,N,P,R,T,V,X,Z,AB,AD,AF,AH,AJ,AL,AN,AP,AR')
column_names=year2006.iloc[3]
year2006=year2006[7:321]
year2006.columns=column_names
year2006.rename(columns={year2006.columns[0]:'city_cn'},inplace=True)
#for population
year2006_1=pd.read_excel('2006_0.xls',usecols='A,B')
column_names=year2006_1.iloc[1]
year2006_1=year2006_1[5:319]
year2006_1.columns=column_names
year2006_1.rename(columns={year2006_1.columns[0]:'city_cn'},inplace=True)
###for em and um
year2006_2=pd.read_excel('2006_1.xls',usecols='A,B,D,F')
column_names=year2006_2.iloc[1]
year2006_2=year2006_2[5:319]
year2006_2.columns=column_names
year2006_2.rename(columns={year2006_2.columns[0]:'city_cn'},inplace=True)
#for gdp
year2006_3=pd.read_excel('2006_2.xls',usecols='A,B')
column_names=year2006_3.iloc[1]
year2006_3=year2006_3[4:318]
year2006_3.columns=column_names
year2006_3.rename(columns={year2006_3.columns[0]:'city_cn'},inplace=True)
###for gov_exp
year2006_4=pd.read_excel('2006_3.xls',usecols='A,C')
column_names=year2006_4.iloc[3]
year2006_4=year2006_4[7:321]
year2006_4.columns=column_names
year2006_4.rename(columns={year2006_4.columns[0]:'city_cn'},inplace=True)
###for wage
year2006_5=pd.read_excel('2006_4.xls',usecols='A,F')
column_names=year2006_5.iloc[1]
year2006_5=year2006_5[5:319]
year2006_5.columns=column_names
year2006_5.rename(columns={year2006_5.columns[0]:'city_cn'},inplace=True)
##for ridership
year2006_6=pd.read_excel('2006_6.xls',usecols='A,B,C,D,E,F')
column_names=year2006_6.iloc[1]
year2006_6=year2006_6[4:318]
year2006_6.columns=column_names
year2006_6.rename(columns={year2006_6.columns[0]:'city_cn'},inplace=True)
##combine into one year
year_2006=year2006.merge(year2006_1.merge(year2006_2.merge(year2006_3.merge(year2006_4.merge(year2006_5.merge(year2006_6,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2006['year']=2006
year_2006.columns=['city_cn','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','Population','employ1','employ2','unemployment','gdp','gov_exp','wage','total_ride','rail','road','water','air','year']
#unit=['employ1','unemployment','air','wage']
#year_2006[unit]=year_2006[unit]/10000









#######year 2007
year_2007=pd.read_excel('2008.xlsx',usecols='A,C,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AD,AH,AI,AJ,AN,AP,AQ')
column_names=year_2007.iloc[1]
year_2007=year_2007[3:]
year_2007.columns=column_names
year_2007.rename(columns={year_2007.columns[0]:'city_cn'},inplace=True)
year_2007['year']=2007
year_2007.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','road','water','air','wage','total_ride','rail','year']
#unit=['employ1','unemployment','air','wage']
#year_2007[unit]=year_2007[unit]/10000





#####year 2008
year_2008=pd.read_excel('2009.xlsx',sheet_name='Sheet1',usecols='A,C,E:AA,AD,AH,AI,AJ,AN,AO,AP')
column_names=year_2008.iloc[0]
year_2008=year_2008[2:]
year_2008.columns=column_names
year_2008.rename(columns={year_2008.columns[0]:'city_cn'},inplace=True)
year_2008['year']=2008
year_2008.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','road','water','air','wage','total_ride','rail','year']
#unit=['employ1','unemployment','air','wage']
#year_2008[unit]=year_2008[unit]/10000


###year 2009
year_2009=pd.read_excel('2010.xls',sheet_name='Sheet1',usecols='A,B,H,J,L,N,P,R,T,V,X,Z,AB,AD,AF,AH,AJ,AL,AN,AP,AR,AT,AV,AX,AZ,BA,BB:BG')
year_2009=year_2009[6:]
year_2009.rename(columns={year_2009.columns[0]:'city_cn'},inplace=True)
year_2009['year']=2009
#unit=['employ1','unemployment','air','wage']
#year_2009[unit]=year_2009[unit]/10000




####year 2010
year_2010=pd.read_excel('2010_0.xls',usecols='A,B,H,J,L,N:V,X,Z,AB,AD,AF,AH,AJ,AL,AN,AP,AR,AT,AV,AX,AZ,BB,BD,BF')
year_2010=year_2010[7:]
year_2010.rename(columns={year_2010.columns[0]:'city_cn'},inplace=True)
year_2010['year']=2010


####year 2011
year_2011=pd.read_excel('2012.xlsx',usecols='A,C,E:AA,AD,AH,AI,AJ,AP,AR,AS')
column_names=year_2011.iloc[0]
year_2011=year_2011[2:]
year_2011.columns=column_names
year_2011.rename(columns={year_2011.columns[0]:'city_cn'},inplace=True)
year_2011['year']=2011
year_2011.columns=['city_cn','Population','employ1','employ2','unemployment','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','gdp','gov_exp','road','water','air','wage','total_ride','rail','year']




##year 2012
year_2012=pd.read_excel('2013.xlsx',usecols='A,C,I,K,M,O,Q,S,U,W,Y,AA,AC,AE,AG,AI,AK,AM,AO,AQ,AS,AU,AW,AY,BA,BH,BL:BP,BW')
year_2012=year_2012[3:]
year_2012.rename(columns={year_2012.columns[0]:'city_cn'},inplace=True)
year_2012['year']=2012






###year2013
##population
population=pd.concat(pd.read_excel('2013_0.xls', sheet_name=None, skiprows=1))
population=population.iloc[:,[0,2]]
#population=population[5:]
population.rename(columns={population.columns[0]:'city_cn',population.columns[1]:'Population'},inplace=True)
city_cn=pd.read_excel('city_cn_2013.xlsx')
pop=population.merge(city_cn,on='city_cn',how='inner')
#employment
employment=pd.concat(pd.read_excel('2013_1.xls', sheet_name=None, skiprows=1))
employment=employment.iloc[:,[0,2,4,6]]
#employment=employment[5:]
employment.rename(columns={employment.columns[0]:'city_cn',employment.columns[1]:'employ1',employment.columns[2]:'employ2',employment.columns[3]:'unemployment'},inplace=True)
em=employment.merge(city_cn,on='city_cn',how='inner')
#gdp
gdp_total=pd.read_excel('2013_2.xls',usecols='A,C')
gdp_total.rename(columns={gdp_total.columns[0]:'city_cn',gdp_total.columns[1]:'gdp'},inplace=True)
gdp=gdp_total.merge(city_cn,on='city_cn',how='inner')
#gov_exp
gov_total=pd.read_excel('2013_3.xls',usecols='A,D')
gov_total.rename(columns={gov_total.columns[0]:'city_cn',gov_total.columns[1]:'gov_exp'},inplace=True)
gov=gov_total.merge(city_cn,on='city_cn',how='inner')
##wage
wage_total=pd.read_excel('2013_4.xls',usecols='A,G')
wage_total.rename(columns={wage_total.columns[0]:'city_cn',wage_total.columns[1]:'wage'},inplace=True)
wage=wage_total.merge(city_cn,on='city_cn',how='inner')
###ridership
ride_total=pd.read_excel('2013_6.xls',usecols='A,C:G')
ride_total.columns=['city_cn','total_ride','rail','road','water','air']
ride=ride_total.merge(city_cn,on='city_cn',how='inner')
###industry employment
lis=['2-5.xls','2-6.xls','2-7.xls','2-8.xls','2-10.xls']
ind_em=city_cn
for excel in lis:
    if excel!='2-10.xls':
        df=pd.concat(pd.read_excel(excel, usecols='A,C,E,G', sheet_name=None, skiprows=1),sort=True)
    else:
        df=pd.concat(pd.read_excel(excel, usecols='A,C,E,G,I', sheet_name=None, skiprows=1),sort=True)
    #df=df.iloc[:,[0,2,4,6]]
    df.rename(columns={df.columns[0]:'city_cn'},inplace=True)
    df1=df.merge(city_cn,on='city_cn',how='inner')
    ind_em=ind_em.merge(df1,on='city_cn',how='inner')
df=pd.concat(pd.read_excel('2-9.xls', sheet_name=None, skiprows=1),sort=True) 
df=df.iloc[:,[0,2,3,4]]  
df.rename(columns={df.columns[0]:'city_cn'},inplace=True)
df1=df.merge(city_cn,on='city_cn',how='inner')
ind_em=ind_em.merge(df1,on='city_cn',how='inner')   
ind_em.columns=['city_cn','ind1','ind2','ind3','ind4','ind5','ind6','ind7','ind8','ind9','ind10','ind11','ind12','ind16','ind17','ind18','ind19','ind13','ind14','ind15']
#year2013 combine
year_2013=pop.merge(em.merge(gdp.merge(gov.merge(wage.merge(ind_em.merge(ride,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2013['year']=2013




######industries start to change
########year 2014
em_2014=pd.read_excel('employ_2015.xlsx',usecols='A,B,D,F',skiprows=4)
em_2014.columns=['city_cn','employ1','employ2','unemployment']
####
gdp_2014=pd.read_excel('gdp_2015.xlsx',usecols='A,B,I,L:P,Z',skiprows=3)
gdp_2014.columns=['city_cn','gdp','gov_exp','total_ride','rail','road','water','air','wage']
####
pop_2014=pd.read_excel('population_2015.xlsx',usecols='A,B',skiprows=3)
pop_2014.columns=['city_cn','Population']
####
ind_2014=pd.read_excel('industry_2015.xlsx',usecols='A,D,F,H,J,L,N,P,R,T,V,X,Z,AB,AD,AF,AH,AJ,AL,AN',skiprows=4)
ind_2014.columns=['city_cn','ind1','ind2','ind3','ind4','ind5','ind8','ind6','ind9','ind7','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19']
#year2014 combine
year_2014=em_2014.merge(gdp_2014.merge(ind_2014.merge(pop_2014,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2014['year']=2014






####year 2015
city_cn=pd.read_excel('2016.xlsx',sheet_name='name')
######
gov_exp=pd.read_excel('2016.xlsx',sheet_name='gov_exp',usecols='A,D')
gov_exp.columns=['city_cn','gov_exp']
gov_2015=gov_exp.merge(city_cn,on='city_cn',how='inner')
####
gdp=pd.read_excel('2016.xlsx',sheet_name='gdp',usecols='A,C')
gdp.columns=['city_cn','gdp']
gdp_2015=gdp.merge(city_cn,on='city_cn',how='inner')
###ride
ride=pd.read_excel('2016.xlsx',sheet_name='ride',usecols='A,C,E,G')
ride.columns=['city_cn','road','water','air']
ride_2015=ride.merge(city_cn,on='city_cn',how='inner')
##wage
wage=pd.read_excel('2016.xlsx',sheet_name='wage',usecols='A,G')
wage.columns=['city_cn','wage']
wage_2015=wage.merge(city_cn,on='city_cn',how='inner')
##ind
lis=['em1','em2','em3','em4','em5','em6']
ind_2015=city_cn
for sheet in lis:
    if sheet != 'em6':
        df=pd.read_excel('2016.xlsx',sheet_name=sheet,usecols='A,C,E,G')
    else:
        df=pd.read_excel('2016.xlsx',sheet_name=sheet,usecols='A,C,E,G,I')
    df.rename(columns={df.columns[0]:'city_cn'},inplace=True)
    df1=df.merge(city_cn,on='city_cn',how='inner')
    #print(df1.shape)
    ind_2015=ind_2015.merge(df1,on='city_cn',how='inner')
    #print(ind_2015.shape)
ind_2015.columns=['city_cn','ind1','ind2','ind3','ind4','ind5','ind8','ind6','ind9','ind7','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19']

####pop
pop=pd.read_excel('2016.xlsx',sheet_name='pop',usecols='A,C')
pop.columns=['city_cn','Population']
pop_2015=pop.merge(city_cn,on='city_cn',how='inner')
####employ
em=pd.read_excel('2016.xlsx',sheet_name='employ',usecols='A,C,E,G')
em.columns=['city_cn','employ1','employ2','unemployment']
em_2015=em.merge(city_cn,on='city_cn',how='inner')


###combine for 2015
year_2015=ind_2015.merge(gdp_2015.merge(gov_2015.merge(ride_2015.merge(pop_2015.merge(em_2015.merge(wage_2015,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2015['year']=2015

##year 2016
city_cn=pd.read_excel('2017.xlsx',sheet_name='name')
######
gov_exp=pd.read_excel('2017.xlsx',sheet_name='gov_exp',usecols='A,D')
gov_exp.columns=['city_cn','gov_exp']
gov_2016=gov_exp.merge(city_cn,on='city_cn',how='inner')
####
gdp=pd.read_excel('2017.xlsx',sheet_name='gdp',usecols='A,C')
gdp.columns=['city_cn','gdp']
gdp_2016=gdp.merge(city_cn,on='city_cn',how='inner')
###ride
ride=pd.read_excel('2017.xlsx',sheet_name='ride',usecols='A,C,D,E')
ride.columns=['city_cn','road','water','air']
ride_2016=ride.merge(city_cn,on='city_cn',how='inner')
##wage
wage=pd.read_excel('2017.xlsx',sheet_name='wage',usecols='A,G')
wage.columns=['city_cn','wage']
wage_2016=wage.merge(city_cn,on='city_cn',how='inner')
##ind
lis=['em1','em2','em3','em4','em5','em6']
ind_2016=city_cn
for sheet in lis:
    if sheet != 'em6':
        df=pd.read_excel('2017.xlsx',sheet_name=sheet,usecols='A,C,E,G')
    else:
        df=pd.read_excel('2017.xlsx',sheet_name=sheet,usecols='A,C,E,G,I')
    df.rename(columns={df.columns[0]:'city_cn'},inplace=True)
    df1=df.merge(city_cn,on='city_cn',how='inner')
    #print(df1.shape)
    ind_2016=ind_2016.merge(df1,on='city_cn',how='inner')
    #print(ind_2015.shape)
ind_2016.columns=['city_cn','ind1','ind2','ind3','ind4','ind5','ind8','ind6','ind9','ind7','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19']

####pop
pop=pd.read_excel('2017.xlsx',sheet_name='pop',usecols='A,C')
pop.columns=['city_cn','Population']
pop_2016=pop.merge(city_cn,on='city_cn',how='inner')
####employ
em=pd.read_excel('2017.xlsx',sheet_name='employ',usecols='A,C,E,G')
em.columns=['city_cn','employ1','employ2','unemployment']
em_2016=em.merge(city_cn,on='city_cn',how='inner')


###combine for 2016
year_2016=ind_2016.merge(gdp_2016.merge(gov_2016.merge(ride_2016.merge(pop_2016.merge(em_2016.merge(wage_2016,on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner'),on='city_cn',how='inner')
year_2016['year']=2016

####year2017
year_2017=pd.read_excel('year2017.xlsx')
year_2017['year']=2017


####convert string to numeric
names=[year_2003,year_2004,year_2005,year_2006,year_2007,year_2008,year_2009,year_2010,year_2011,year_2012,year_2013,year_2014,year_2015,year_2016]
for name in names:
    for d in name.columns:
        if d is not 'city_cn':
            #name[d] = name[d].replace('\D','', regex=True) 
            name[d] = pd.to_numeric(name[d], errors='coerce')

###change into the same unit
unit=['employ2','unemployment','air','wage']
unit_2011=['employ2','unemployment','wage']
unit_2014=['ind1','ind2','ind3','ind4','ind5','ind8','ind6','ind9','ind7','ind10','ind11','ind12','ind13','ind14','ind15','ind16','ind17','ind18','ind19','employ1','employ2','unemployment','wage']

year_2003[unit]=year_2003[unit]/10000
year_2004[unit]=year_2004[unit]/10000
year_2005[unit]=year_2005[unit]/10000
year_2006[unit]=year_2006[unit]/10000
year_2007[unit]=year_2007[unit]/10000
year_2008[unit]=year_2008[unit]/10000
year_2009[unit]=year_2009[unit]/10000
year_2010[unit]=year_2010[unit]/10000
year_2011[unit_2011]=year_2011[unit_2011]/10000
year_2012[unit_2011]=year_2012[unit_2011]/10000
year_2013[unit_2011]=year_2013[unit_2011]/10000
year_2014[unit_2014]=year_2014[unit_2014]/10000
year_2015[unit_2014]=year_2015[unit_2014]/10000
year_2016[unit_2014]=year_2016[unit_2014]/10000
year_2017[unit_2014]=year_2017[unit_2014]/10000

city_cn_2003=year_2003['city_cn']
year_2017=year_2017.merge(city_cn_2003,on='city_cn',how='right')
year_2016=year_2016.merge(city_cn_2003,on='city_cn',how='right')
year_2015=year_2015.merge(city_cn_2003,on='city_cn',how='right')
year_2014=year_2014.merge(city_cn_2003,on='city_cn',how='right')
year_2013=year_2013.merge(city_cn_2003,on='city_cn',how='right')
year_2012=year_2012.merge(city_cn_2003,on='city_cn',how='right')
year_2011=year_2011.merge(city_cn_2003,on='city_cn',how='right')
year_2010=year_2010.merge(city_cn_2003,on='city_cn',how='right')
year_2009=year_2009.merge(city_cn_2003,on='city_cn',how='right')
year_2008=year_2008.merge(city_cn_2003,on='city_cn',how='right')
year_2007=year_2007.merge(city_cn_2003,on='city_cn',how='right')
year_2006=year_2006.merge(city_cn_2003,on='city_cn',how='right')
year_2005=year_2005.merge(city_cn_2003,on='city_cn',how='right')
year_2004=year_2004.merge(city_cn_2003,on='city_cn',how='right')

names1=[year_2003,year_2004,year_2005,year_2006,year_2007,year_2008,year_2009,year_2010,year_2011,year_2012,year_2013,year_2014,year_2015,year_2016,year_2017]
variables=pd.concat(names1,sort=False)
variables.to_excel('variables.xlsx',index=None)

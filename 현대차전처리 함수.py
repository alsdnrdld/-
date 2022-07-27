#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[46]:


def EDA_DEF(df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = pd.read_excel(df)
    df = df.drop(['Unnamed: 15'],axis=1)
    clist = ['Region','Category','Model','1','2','3','4','5','6','7','8','9','10','11','12']
    df.columns = clist
    df[df['Category'].str.contains('Dom',na= False)] # 4부터
    df[df['Category'].str.contains('Ex',na= False)]  # 48까지 Dom
    df_dom = df[4:48]
    df_ex = df[49:]
    df_dom['Region'] = 'Domestic'
    df_ex.reset_index(inplace=True, drop='True')
    df_dom.reset_index(inplace=True, drop='True')
    df_dom= df_dom[2:]
    df_dom.reset_index(inplace=True, drop='True')
    df_dom[df_dom['Category'].str.contains('RV',na=False)] # 23까지 PC
    df_dom[df_dom['Category'].str.contains('CV',na=False)]# 24부터 37까지 RV, 40이후부터 쭉 CV
    df_dom['Category'][:24]='PC'
    df_dom['Category'][24:38]='RV'
    df_dom['Category'][37:]='CV'
    a = df_dom[:40]
    a = a.drop(a[a['Model'].str.contains('Sub',na=False)].index)
    b= a.dropna(subset=["Model"])
    b=b.fillna(0)
    df_ex['Region'] = 'Export'
    df_ex.reset_index(inplace=True, drop='True')
    c = df_ex[2:]
    c.reset_index(inplace=True,drop=True)
    c[c['Category'].str.contains('RV',na=False)] #23까지 PC
    c[c['Category'].str.contains('CV',na=False)] # 24부터 40까지는 RV, 41이후부터 전부 CV
    c['Category'][:24]='PC'
    c['Category'][24:41]='RV'
    c['Category'][41:]='CV'
    c= c.drop(c[c['Model'].str.contains('Sub',na=False)].index)
    c.reset_index(inplace= False,drop=True)
    c= c[:-3]
    c=c.dropna(subset=["Model"])
    c = c.fillna(0)
    c['Year']=2020
    b['Year']=2020
    d = pd.concat([b,c])
    dc2 = d.melt(id_vars=['Region','Category','Model','Year'],value_vars=['1','2','3','4','5','6','7','8','9','10','11','12']).sort_values('Category')
    dc2.rename(columns = {'variable':'Month','value':'Sales'},inplace=True)
    dc2.to_excel('./현대차 전처리파일들/hmc_2020_pivot_1.xlsx',index=False)
   
    return pd.DataFrame(dc2)


# In[36]:


df= './Hyundae_Car/hmc-sales-by-model-y2020.xlsx'


# In[47]:


EDA_DEF(df)


# In[ ]:


df[df['Category'].str.contains('Dom',na= False)] # 4부터
   df[df['Category'].str.contains('Ex',na= False)]  # 48까지 Dom
   df_dom = df[4:48]
   df_ex = df[49:]
   df_dom['Region'] = 'Domestic'
   df_ex.reset_index(inplace=True, drop='True')
   df_dom.reset_index(inplace=True, drop='True')
   df_dom= df_dom[2:]
   df_dom.reset_index(inplace=True, drop='True')
   df_dom[df_dom['Category'].str.contains('RV',na=False)] # 23까지 PC
   df_dom[df_dom['Category'].str.contains('CV',na=False)]# 24부터 37까지 RV, 40이후부터 쭉 CV
   df_dom['Category'][:24]='PC'
   df_dom['Category'][24:38]='RV'
   df_dom['Category'][37:]='CV'
   a = df_dom[:40]
   a = a.drop(a[a['Model'].str.contains('Sub',na=False)].index)
   b= a.dropna(subset=["Model"])
   b=b.fillna(0)
   df_ex['Region'] = 'Export'
   df_ex.reset_index(inplace=True, drop='True')

   c = df_ex[2:]
   c.reset_index(inplace=True,drop=True)
   c[c['Category'].str.contains('RV',na=False)] #23까지 PC
   c[c['Category'].str.contains('CV',na=False)] # 24부터 40까지는 RV, 41이후부터 전부 CV
   c['Category'][:24]='PC'
   c['Category'][24:41]='RV'
   c['Category'][41:]='CV'
   c= c.drop(c[c['Model'].str.contains('Sub',na=False)].index)
   c.reset_index(inplace= False,drop=True)
   c= c[:-3]
   c=c.dropna(subset=["Model"])
   c = c.fillna(0)
   c['Year']=2020
   b['Year']=2020
   d = pd.concat([b,c])
   dc2 = d.melt(id_vars=['Region','Category','Model','Year'],value_vars=['1','2','3','4','5','6','7','8','9','10','11','12']).sort_values('Category')
   dc2.rename(columns = {'variable':'Month','value':'Sales'},inplace=True)
   dc2.to_excel('./현대차 전처리파일들/hmc_2020_pivot_1.xlsx',index=False)


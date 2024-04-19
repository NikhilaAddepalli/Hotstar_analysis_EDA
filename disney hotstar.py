#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("disney_plus_titles.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


data.describe()


# In[7]:


data.columns


# In[8]:


data.nunique()


# In[9]:


data['country'].unique()


# In[10]:


data['rating'].unique()


# In[11]:


data.isnull().sum()


# In[12]:


disney_plus_titles=data.drop(['date_added'],axis=1)


# In[13]:


data.columns


# In[14]:


data.duplicated()


# In[15]:


corelation=disney_plus_titles.corr()


# In[16]:


sns.heatmap(corelation,xticklabels=corelation.columns,yticklabels=corelation.columns,annot=True)


# In[41]:


data_director = data.assign(var1 = data.director.str.split(',')).explode('var1').reset_index(drop = True)

data_director['splitted'] = data_director.var1.str.lstrip()


# In[18]:


pip install  plotly.express


# In[19]:


director = pd.DataFrame(data_director['splitted'].value_counts()).reset_index().head(20)
fig = px.bar(director,director['index'],director['splitted'],labels={'index':'name','splitted':'count'})
fig.update_layout(title='Top 20 directors',title_x=0.9)


# In[45]:


rl_years = data['release_year'].value_counts()

plt.figure(figsize=(6,6))
sns.lineplot(x=rl_years.index, y=rl_years.values, data=rl_years)
plt.title('Number of releases by year',fontsize=17)
plt.xticks(np.arange(1930, 2022, 10), rotation=320)
plt.show()


# In[ ]:





# In[ ]:





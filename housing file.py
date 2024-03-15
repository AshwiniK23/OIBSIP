#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns
import os 


# In[2]:


os.chdir(r"C:\Users\hp\Downloads\internship")


# In[3]:


df=pd.read_csv("Housing.csv")


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.nunique()


# In[12]:


df.corr()


# In[13]:


df.skew()


# In[14]:


df.isnull()


# In[15]:


df.isnull().sum()


# In[16]:


df["price"].value_counts


# In[17]:


df["area"].value_counts


# In[18]:


pd.get_dummies(df, drop_first=True)  


# In[19]:


df_dum = pd.get_dummies(df, drop_first=True) 


# In[20]:


df_dum


# In[21]:


sns.pairplot(df) 
plt.show()


# In[22]:


sns.lineplot(x="price",y="area",data=df)
plt.show()


# In[ ]:





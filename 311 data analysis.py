#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


url = "https://data.cityofnewyork.us/resource/3rfa-3xsf.json"


# In[3]:


dataset = pd.read_json(url)


# In[4]:


dataset


# In[5]:


dataset = dataset.drop(dataset.columns[[0, 1, 2,3,4]], axis=1)


# In[6]:


dataset


# In[7]:


dataset = dataset.drop(dataset.columns[[-1, -2, -3]], axis=1)


# In[8]:


dataset


# In[9]:


status_update = dataset['status']


# In[10]:


from matplotlib import pyplot as plt 


# In[11]:


total_status = status_update.index


# In[12]:


indexcountoftotal = len(total_status)


# In[13]:


indexcountoftotal


# In[14]:


grouped =dataset.groupby('status')


# In[15]:


C = grouped.get_group('Closed')


# In[16]:


O =grouped.get_group('Open')
P =grouped.get_group('Pending')


# In[17]:


percentageofclosed = ( len(C) / indexcountoftotal )*100


# In[18]:


percentageofOpen = ( len(O) / indexcountoftotal )*100


# In[19]:


percentageofPending = ( len(P) / indexcountoftotal )*100


# In[20]:


percentageofclosed


# In[21]:


percentageofOpen


# In[22]:


percentageofPending


# In[23]:


others = 100 -(percentageofclosed+percentageofOpen+percentageofPending)


# In[24]:


others


# In[25]:


import matplotlib.pyplot as plt


labels = 'Closed', 'Open', 'Pending', 'Others'
sizes = [percentageofclosed,percentageofOpen,percentageofPending,others]
explode = (0.1, 1, 1, 1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()


# In[26]:


dataset['status'].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()


# In[34]:


dataset['borough'].value_counts().plot(kind='bar',alpha=0.6,)
plt.show()


# In[ ]:





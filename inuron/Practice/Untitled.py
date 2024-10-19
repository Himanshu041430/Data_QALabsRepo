#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.DataFrame({'year':[2015, 2016],
                    'month':[2,3],
                     'day':[4,5]})


# In[4]:


pd.to_datetime(df)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


from dtm import Dtmodel
from dtm import Download


# In[11]:


d = Download()


# In[12]:


d.download_file()


# In[13]:


m = Dtmodel()


# In[14]:


m.train()


# In[15]:


print(m.predict())


# In[ ]:





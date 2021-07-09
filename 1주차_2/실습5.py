#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip list')


# In[2]:


help('sys')


# In[3]:


import os


# In[4]:


os.getcwd()


# In[5]:


os.listdir()


# In[6]:


import numpy as np


# In[7]:


np.absolute(-3)


# In[8]:


np.sqrt(16)


# In[9]:


from scipy import stats


# In[10]:


stats.hmean([1, 2, 3])


# In[11]:


stats.variation([1,2,3])


# In[12]:


from datetime import datetime


# In[13]:


now = datetime.now()


# In[14]:


now.year


# In[15]:


now.month


# In[16]:


import sys


# In[17]:


sys.path


# In[18]:


import myprint


# In[19]:


hello = 'Hello World Python'


# In[20]:


myprint.print1(hello)


# In[21]:


myprint.print2(hello)


# In[22]:


from mymodule import myprint2


# In[23]:


myprint2.print3(hello)


# In[24]:


myprint2.print4(hello)


# In[ ]:





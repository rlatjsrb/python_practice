#!/usr/bin/env python
# coding: utf-8

# In[11]:


set1 = {'A', 'B', 'C', 'A', 'D', 'E', 'F', 'B'}
set1


# In[12]:


set1[0]


# In[13]:


set1[:5]


# In[14]:


set1.add('a')
set1


# In[15]:


set1.add('A')
set1


# In[16]:


set1.remove('a')
set1


# In[17]:


set1.pop()
set1


# In[24]:


set1 = {'A','B','C','D','E','F'}
set2 = {'B','D','G','H'}


# In[25]:


set1 & set2


# In[26]:


set1.intersection(set2)


# In[27]:


set1 | set2


# In[28]:


set1.union(set2)


# In[29]:


set1 - set2


# In[30]:


set1.difference(set2)


# In[31]:


set1 ^ set2


# In[33]:


set1.symmetric_difference(set2)


# In[34]:


중간고사 = {
    '수학' : 100,
    '영어' : 90,
}
중간고사


# In[36]:


중간고사['국어'] = 85
중간고사


# In[37]:


중간고사['영어']


# In[38]:


중간고사['영어'] = 95
중간고사


# In[39]:


list(중간고사.keys())


# In[40]:


list(중간고사.values())


# In[41]:


중간고사.items()


# In[42]:


중간고사.pop('국어')


# In[43]:


중간고사


# In[ ]:





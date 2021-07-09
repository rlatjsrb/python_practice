#!/usr/bin/env python
# coding: utf-8

# In[1]:


letter1 = ['A', 'B', 'C']


# In[2]:


letter2 = ['D', 'E', 'F']


# In[3]:


letter1 + letter2


# In[4]:


list_num1 = [1, 2, 3]


# In[5]:


list_num2 = [4, 5, 6]


# In[6]:


list_num1 + list_num2


# In[7]:


'A' in letter1


# In[8]:


'A' in letter2


# In[9]:


letters = ['A', 'B', 'C', 'D', 'E', 'F']


# In[10]:


letters


# In[11]:


letters[0] = 'a' 
letters


# In[12]:


letters[0] = 'A' 
letters


# In[13]:


letters[6] = 'a'


# In[14]:


len(letters)


# In[15]:


letters.count('A')


# In[16]:


letters.append('a')
letters


# In[17]:


letters.insert(2, 'z')
letters


# In[18]:


letters.pop(2)


# In[19]:


letters


# In[20]:


letters.remove('a')
letters


# In[21]:


letters.sort(reverse=True)


# In[22]:


letters


# In[23]:


letters.sort()


# In[24]:


letters


# ---

# In[25]:


letters[0]


# In[26]:


letters[5]


# In[27]:


letters[-1]


# In[28]:


letters[-2]


# In[29]:


letters[0:3]


# In[30]:


letters[3:]


# In[31]:


letters[:4]


# In[32]:


letters[:]


# In[33]:


letters[::2]


# In[36]:


letters[::-1]


# In[37]:


tuple1 = ('A', 'B', 'C', 'D', 'E')
tuple1


# In[38]:


tuple1[0] = 'a'


# In[39]:


tuple1.index('C')


# In[40]:


tuple1.count('A')


# In[41]:


list1 = list(tuple1)


# In[42]:


list1.append('a')
list1


# In[43]:


tuple2 = tuple(list1)
tuple2


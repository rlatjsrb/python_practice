#!/usr/bin/env python
# coding: utf-8

# In[1]:


fr = open('./12-1. hello.txt','r')


# In[2]:


for line in fr:
    print(line)


# In[3]:


fr.close()


# In[4]:


with open('./12-1. hello.txt','r') as fr:
    for line in fr:
        print(line)


# In[11]:


fw = open('./hello_write.txt', 'w')


# In[12]:


fw.write('Hello World Python!!!\n')


# In[13]:


fw.write('Welcome to Python World!!!\n')


# In[14]:


fw.close()


# In[15]:


with open('./hello_write.txt', 'x') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!')


# In[16]:


with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# In[18]:


import os


# In[20]:


os.listdir('.')


# In[21]:


file_list = os.listdir('.')


# In[23]:


file_ipynb = [f for f in file_list if f.endswith('ipynb')]


# In[24]:


file_ipynb


# In[25]:


os.getcwd()


# In[26]:


os.mkdir('test')


# In[27]:


os.path.join('.','test')


# In[28]:


os.path.abspath('hello.txt')


# In[29]:


os.path.isfile('hello_write.txt')


# In[30]:


os.path.isdir('hello_write.txt')


# In[32]:


os.path.isfile('test')


# In[33]:


os.path.isdir('test')


# In[34]:


os.path.split(os.path.abspath('hello_write.txt'))


# In[35]:


os.path.splitext('hello_write.txt')


# In[ ]:





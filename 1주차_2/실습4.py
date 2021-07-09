#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add1():
    print('더하기 함수입니다.')


# In[2]:


add1()


# In[3]:


def add2(x, y):
    print(x + y)


# In[4]:


add2(1, 2)


# In[6]:


def add3():
    x, y = 2, 4
    return x + y


# In[7]:


re_val = add3()
print(re_val)


# In[8]:


def add4(x, y):
    return x + y


# In[9]:


re_val = add4(2, 4)
print(re_val)


# In[10]:


def square(x, y):
    x = x ** 2
    y = y ** 2
    return x, y


# In[11]:


a, b = square(2, 3)
print(a)
print(b)


# In[12]:


def square2(x = 2, y = 3):
    x = x ** 2
    y = y ** 2
    return x, y


# In[13]:


square2()


# In[14]:


square2(2)


# In[15]:


square2(2, 3)


# In[17]:


def square2(x = 2, y = 3):
    x = x ** 2
    y = y ** 2
    return x, y


# In[18]:


square2(4, 5)


# In[21]:


square2(y = 5, x = 4)


# In[23]:


def changeble(x, *y):
    print(x, y)


# In[24]:


changeble(1)


# In[25]:


changeble(1, 2)


# In[26]:


changeble(1, 2, 3)


# In[27]:


changeble(1,2,3,4,5)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ### 파이썬 연산자

# 더하기

# In[1]:


2 + 4


# 빼기

# In[8]:


4 - 2

곱하기
# In[9]:


2 * 4


# 나누기

# In[10]:


4 / 2


# 제곱

# In[4]:


4 ** 2


# 몫

# In[11]:


7 / 2


# 정수몫

# In[6]:


7 // 2


# 나머지

# In[7]:


7 % 2


# ----------------------------------------------------------------------------------------------------------------

# ### 파이썬 주석문

# In[12]:


# ctrl + /


# In[13]:


# 파이썬 주석문


# In[14]:


# 파이썬
# 주석문


# In[15]:


'''
파이썬
블럭
주석문
'''
print(1)


# ### 들여쓰기

# In[16]:


a = True
if a:
    print("True")
else:
    print("False")


# In[18]:


a = True
if a:
    print("True")
    print("True End ...")
else:
    print("False")
print('End...')


# In[ ]:





# ### print 함수

# In[1]:


print('Hello world Python')


# In[2]:


print('a', 1)


# In[3]:


print('a', 1, sep = ':')


# In[4]:


print('a', 1, sep = ':', end = '.')


# ### input 함수

# In[5]:


input()


# In[7]:


input('프로그램 언어 : ')


# In[8]:


round(3.141592)


# In[9]:


round(3.141592, 2)


# In[10]:


round(3.142592, 5)


# In[11]:


max(10, 100, 1000)


# In[12]:


min(10, 100, 1000)


# In[13]:


pow(2, 4) # 2**4


# In[14]:


len('Hello World Python')


# In[15]:


zip('abc', '123')


# In[16]:


list(zip('abc', '123'))


# In[17]:


hello = 'Hello world Python'


# In[18]:


print(hello)


# In[19]:


hello


# In[20]:


hello
hello


# In[21]:


print(hello)
print(hello)


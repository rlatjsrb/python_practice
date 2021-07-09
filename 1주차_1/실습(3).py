#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = '파이썬'


# In[6]:


print(type(a))


# In[7]:


print(a)


# In[8]:


b = "문자열"


# In[9]:


print(b)


# In[10]:


c = """
죽는 날까지 하늘을 우러러 
한 점 부끄럼 없기를
잎새에 이는 바람에도
나는 괴로워 했다
"""


# In[11]:


print(c)


# In[12]:


'파이썬' + 3


# In[13]:


d = '파이썬' + str(3)


# In[14]:


print(d)


# In[15]:


e = '*' * 10


# In[16]:


print(e)


# In[17]:


a = 'HelloWorld!'


# In[18]:


a


# In[19]:


a[0]


# In[20]:


a[5]


# In[21]:


a[-1]


# In[22]:


a[-2]


# In[23]:


a[:5] # a[0:5]


# In[24]:


a[5:]


# In[25]:


a[:]


# In[26]:


a[::2]


# In[27]:


a[::-1] #step이 음수는 역정렬


# In[28]:


a[::-2]


# In[29]:


name, age, phone = '홍길동', 25, '010-111-2222'


# In[30]:


소개 = "이름은 {} 이고, 나이는 {}세 이며, 전화번호는 {} 입니다. ".format(name, age, phone)
소개


# In[31]:


소개 = "이름은 {0} 이고, 나이는 {2}세 이며, 전화번호는 {1} 입니다. ".format(name, phone, age)
소개


# In[32]:


소개 = "이름은 {a} 이고, 나이는 {b}세 이며, 전화번호는 {c} 입니다. ".format(c = phone, a = name, b = age)
소개


# In[33]:


소개 = f"이름은 {name} 이고, 나이는 {age}세 이며, 전화번호는 {phone} 입니다. "
소개


# In[34]:


jan, dec = 1, 12


# In[35]:


print("한 해의 시작은 {:02d}월".format(jan))
print("한 해의 마지막은 {:02d}월".format(dec))


# In[36]:


val = 123456789
money = "{:,}"
money.format(val)


# In[37]:


'{}, {:f}, {:.1f}, {:.2f}, {:.2%}'.format(3, 3, 3, 3.1415, 1/3)


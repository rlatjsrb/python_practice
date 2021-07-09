#!/usr/bin/env python
# coding: utf-8

# In[3]:


x = 10; y = 5


# In[4]:


x == y


# In[10]:


x != y


# In[11]:


x > y


# In[12]:


x < y


# In[14]:


x >= y


# In[16]:


x <= y


# In[17]:


x = True; y = False


# In[18]:


x and y


# In[19]:


x or y


# In[20]:


not x


# In[21]:


x, y = 10, 5


# In[22]:


if x > y:
    print('x가 y보다 큽니다.')


# In[23]:


x, y = 5, 10


# In[24]:


if x > y:
    print('x가 y보다 큽니다.')
else:
    print('x가 y보다 작습니다.')


# In[25]:


x, y = 10, 10


# In[26]:


if x > y:
    print('x가 y보다 큽니다.')
elif x == y:
    print('x와 y가 같습니다.')
elif x < y:
    print('x가 y보다 작습니다.')


# In[27]:


score = 90


# In[28]:


if score >= 90:
    print('A학점입니다.')
elif score >= 80:
    print('B학점입니다.')
elif score >= 70:
    print('C학점입니다.')
elif score >= 60:
    print('D학점입니다.')
else:
    print('F학점입니다.')


# In[29]:


a = True
if a:
    print('a는 True입니다.')
    print('True End...')
else:
    print('a는 False입니다.')
print('False End...')


# In[30]:


a = True
if a:
    print('a는 True입니다.')
    print('True End...')
else:
    print('a는 False입니다.')
    print('False End...')


# In[31]:


a = True
x, y = 5, 10


# In[32]:


if a == True:
    print('a는 True입니다.')
    if x > y:
        print('x가 y보다 큽니다.')
    else:
        print('x가 y보다 작습니다.')
else:
    print('a는 False입니다.')


# In[35]:


나이 = 30
회원 = True


# In[38]:


입장료 = 0

if 회원:
    if 나이 > 6 and 나이 <= 13:
        입장료 = 2500
    elif 나이 > 14 and 나이 <= 59:
        입장료 = 5000
else:
    if 나이 > 6 and 나이 <= 13:
        입장료 = 5000
    elif 나이 > 14 and 나이 <= 59:
        입장료 = 10000

print(f'입장료는 {입장료:,}원 입니다.')


# In[41]:


입장료 = 0

if 나이 <= 6 or 나이 >= 60:
    입장료 = 0
elif 나이 > 6 and 나이 <= 13:
    입장료 = 5000
elif 나이 > 14 and 나이 <= 59:
    입장료 = 10000
    
if 회원:
    입장료 = int(입장료 * 0.5)
    
print(f'입장료는 {입장료:,}원 입니다.')


# In[ ]:





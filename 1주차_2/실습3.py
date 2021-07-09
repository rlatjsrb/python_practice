#!/usr/bin/env python
# coding: utf-8

# In[1]:


for num in [1, 2, 3]:
    print(num)


# In[2]:


for st in ['Hello', 'World', 'Python']:
    print(st)


# In[3]:


score = {'국어':95, '영어':90, '수학':80}


# In[4]:


for item in score.keys():
    print(item)


# In[5]:


for item in score.values():
    print(item)


# In[6]:


for key, value in score.items():
    print(f'{key}과목 점수는 {value}점 입니다.')


# In[7]:


list(range(10))


# In[8]:


list(range(1, 11))


# In[9]:


list(range(10, 0, -1))


# In[10]:


for i in range(1, 11, 2):
    print(i)


# In[11]:


for i in range(0, 11, 2):
    print(i)


# In[12]:


for i in range(1, 10):
    ans = 2 * i
    print(f'2 X {i} = {ans}')
else:
    print('구구단 2단을 종료합니다.')


# In[13]:


a = 0


# In[14]:


while a < 10:
    print(a)
    a += 1
else:
    print(f'a가 {a}이므로 종료합니다.')


# In[15]:


x = 0


# In[16]:


while True:
    x += 3
    print(x)
    if x > 100 and x % 3 == 0:
        break


# In[17]:


list1 = list(range(1, 11))
print(list1)


# In[19]:


list2 = [i*2 for i in list1]
list2


# In[20]:


list1 = list(range(1, 11))
print(list1)


# In[23]:


list3 = [i**2 for i in list1 if i%2 == 1]
list3


# In[ ]:





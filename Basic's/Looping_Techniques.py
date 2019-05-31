#!/usr/bin/env python
# coding: utf-8

# In[1]:


#LOOING

knights = {'aakash': '17', 'Dhaval': '23', 'ashok': '51'}


# In[10]:


[(k,v) for k, v in knights.items()]


# In[11]:


#perfect
for k, v in knights.items():
    print(k, v)


# In[13]:


#NEXT


# In[14]:


for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[15]:


#NEXT


# In[16]:


questions = ['name', 'age', 'fav_color']
answers = ['aakash_padhiyar', '17', 'black']


# In[18]:


for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))


# In[19]:


#NEXT


# In[21]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[22]:


#NEXT


# In[23]:


basket = ['apple', 'orange', 'pear', 'banana', 'orange', 'apple']


# In[24]:


for f in sorted(set(basket)):
    print(f)


# In[25]:


#NEXT


# In[26]:


import math


# In[33]:


raw_data  = [56.5, float('NaN'), 51.8, 78.4, float('NaN')]
print(raw_data)
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data


# In[ ]:


# INFORMATION 

## BY aakashpadhiyar

## BY 8140171224


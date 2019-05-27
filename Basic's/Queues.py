#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque


# In[3]:


queue = deque(['aakash', 'dhaval', 'ashok'])


# In[4]:


queue.append('knao')
queue.append('chiko')


# In[5]:


queue.popleft()


# In[7]:


queue.popleft()


# In[8]:


print(queue)


# In[9]:


#next one


# In[23]:



squares = [x**2 for x in range(10)]

    
print(squares)


# In[24]:


#next


# In[28]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[29]:


#OR


# In[32]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs


# In[31]:


#Next


# In[ ]:





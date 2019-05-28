#!/usr/bin/env python
# coding: utf-8

# In[5]:


[(x, y) for x in [1, 2, 3] for y in [3,1,4] if x != y]


# In[10]:


#NEXT


# In[11]:


vec = [-4, -2, 0, 2, 4]

[x*2 for x in vec]


# In[12]:


#next


# In[13]:


[x for x in vec if x >= 0]


# In[14]:


#NEXT


# In[16]:


[abs(x) for x in vec]


# In[17]:


#NEXT


# In[19]:


freashfruit = ['banana', 'apple', 'passionfruit']


# In[20]:


[weapon.strip() for weapon in freashfruit]


# In[21]:


#NEXT


# In[22]:


[[x, x**2] for x in range(6)]


# In[23]:


#NEXT


# In[30]:


#for error show
[x, x**2 for x in range(6)]


# In[25]:


#NEXT
vec = [[1,2,3], [4,5,6], [7,8,9]]


# In[26]:


[num for elem in vec for num in elem]


# In[31]:


#NEXT


# In[32]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[39]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[ ]:





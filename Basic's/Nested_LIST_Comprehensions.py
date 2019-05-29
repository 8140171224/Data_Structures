#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


# In[8]:


[[row[i] for row in matrix] for i in range(4)]


# In[9]:


#NEXT


# In[11]:


transposed = []

for i in range(4):
    transposed.append([raw[i] for raw in matrix])


# In[12]:


transposed


# In[13]:


#NEXT


# In[14]:


transposed = []

for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# In[15]:


transposed


# In[16]:


#NEXT


# In[22]:


list(zip(*matrix))


# In[ ]:


# INFOEMATION

## BY aakashpadhiyar
## BY 8140171224


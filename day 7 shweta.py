#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Day7 assignment- shweta


# In[2]:


#question


# In[3]:


#Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, and make a new dictionary in which keys become values and values become keys, as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23, "http": 80}


# In[12]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
port2 = {values:keys for keys,values in port1.items()}
print("Port2=",port2)


# In[5]:


#Take a list of tuple as shown below. [(1,2), (3,4), (5,6),(4,5)] Generate a new list which contains sum of number of tuples. For example give Input [(1,2), (3,4), (5,6)] Output [3, 7, 11]


# In[11]:


RequiredList = [(1,2), (3,4), (5,6),(4,5)] 
result = []
for each in range(0,len(RequiredList)):
    a,b = RequiredList[each]
    result.append(a+b)
print("Output",result)


# In[10]:


#Take a list as  given [(1,2,3), [1,2], ['a','hit','less']] The List contains tuple and lists respectively. Make the elements of inner lists and tuples to outer list


# In[9]:


List1 = [(1,2,3), [1,2], ['a','hit','less']] 
List2 = []
List2 = [p for each in List1 for p in each]
print("Output - ",List2)


# In[ ]:





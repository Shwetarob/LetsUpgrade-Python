#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Day3 Assignment -shweta anand


# In[3]:


#question 1 


# In[13]:


#print Sum of n number using while loop


# In[12]:



Num=3
if Num < 0:
    print("Enter the digit greater than Zero")
else:
    Sum=0
    while (Num > 0):
        Sum=Sum+Num
        Num=Num-1
    print("The sum of the number is",Sum)


# In[10]:


#To find out whether prime or not


# In[15]:


Num=10
i=1
if Num>1:
    if Num%i ==0:
        print("Number is not prime",Num)
    else:
        print("Number is prime",Num)
else: 
    print("Number is not prime",Num)


# In[ ]:





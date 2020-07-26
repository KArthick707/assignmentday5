#!/usr/bin/env python
# coding: utf-8

# In[58]:


num = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
b = 0
flag = 1
num.sort()
for i in range(0,len(num)):
    if (num[i] != 0):
        print(num[i])
        if (flag == 1):
            b=i
            flag=0
            
for i  in range(0,b):
    print(0,end="")


# In[60]:


list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
list3 = list1+  list2
list3.sort()
print(list3)
        


# In[63]:


list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45]
l1 = len(list1)
l = len(list2)
for i  in range(l):
    list1.append(list2[i])
for i in range(l):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1], list1[j]
print(list1)


# In[ ]:





# In[ ]:





# In[ ]:





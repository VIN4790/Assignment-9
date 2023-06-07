#!/usr/bin/env python
# coding: utf-8

# In[4]:


def poweroftwo(n):
    if n==0:
        return 1
    else:
        return 2*poweroftwo(n-1)


# In[5]:


poweroftwo(5)


# In[11]:


def poweroftwo(n):
    print("hello")
    i=1
    power=1
    while i<=5:
        power*=2
        i+=1
    return power


# In[12]:


poweroftwo(5)


# In[15]:


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)


# In[ ]:





# In[16]:


factorial(5)


# In[21]:


def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    


# In[22]:


fibonacci(8)


# In[23]:


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 1): return True
        if (n < 1 or n % 4 != 0): return False
        return self.isPowerOfFour(n // 4)


# In[31]:


POF=Solution()
POF.isPowerOfFour(60
                 )


# 1.POWER OF TWO

# In[47]:


def power_of_two(n):
    if n==1:return True
    if n<0 or n%2!=0:return False
    return power_of_two(n//2)
    
    


# In[50]:


power_of_two(3)


# 2.SUM OF FIRST NNATURAL NUMBERS

# In[52]:


def sum_of_numbers(n):
    if n==1:
        return 1
    else:
        return n+sum_of_numbers(n-1)
    


# In[55]:


sum_of_numbers(3)


# 3.FACTORIAL

# In[ ]:


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)


# In[57]:


factorial(5
         )


# 4.POWER OF NUMBER

# In[20]:


def pon(n,p):
    if p==1:
        return n
    else:
        return n*pon(n,p-1)


# In[21]:


pon(5,2)


# 5.Maximum element

# In[29]:


def max_element(arr,i):
    if i==len(arr)-1:
        return arr[i]
    maxim=max_element(arr,i+1)
    return max(maxim,arr[i])
    
    


# In[30]:


max_element([4,10,15,3],0) 


# In[ ]:


6.ARTHEMETIC PROGRESSION


# In[13]:


def ap(i,d,N):
    if N==1:
        return i
    
    return d+ap(i,d,N-1)
    
    
   


# In[14]:


ap(2,1,5)


# In[ ]:


8.Product of array elements


# In[21]:


def product_array(arr,n):
    if n==0:
        return arr[0]
    else:
        return arr[n]*product_array(arr,n-1)

    


# In[22]:


product_array([4,5,2,3],len([4,5,2,3])-1)


# In[ ]:





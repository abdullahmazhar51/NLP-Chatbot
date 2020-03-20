#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pyramid program


# In[44]:


def pattern(n):
    
    #deals with space
    
    k = 2*n-2 
    
    
     #to handle number of rows
        
    for i in range (0, n): 
        
        
        
        #to handle number of spaces 
        
        for j in range(0, k): 
            print(end=" ")
            
             #decrementing k after each loop
                
        k = k - 1  
       
        
        #to handle number of columns
    
    
        for j in range(0, i+1): 
            print("* ", end="")
            
            #ending line after each row
        print("\r")
pattern(5)


# In[23]:


#inverse pyramid


# In[33]:


def pattern(n):
    
    #to deal with spaces
    
    k=2*n-2
    
    #outer no of loops
    for i in range(n,-1,-1):
        
        
        #loops deal with spaces
        for j in range(k, 0, -1):
            print(end=" ")
        
        #incrementing k
        
        k = k+1

        
        # inner no of loops
        for j in range(0, i+1):
      
    
           print("* ", end="")
        
        #ending line after each rows
        
        print("\r")
pattern(5)


# In[34]:


#right star pattern


# In[45]:


def pattern(n):
    for i in range(0,n):
        for j in range(0, i+1):
            
            print("* ", end="")
        print("\r")
    for i in range(n, 0, 1):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattern(5)


# In[49]:


#right star pattern


# In[50]:


def pattern(n):
    for i in range(0,n):
        for j in range(0, i+1):
            
            print("* ", end="")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattern(5)


# In[ ]:


#left star pattern


# In[58]:


def pattern(n):
    k = 2*n-2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k-2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    k = k - 1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
pattern(5)
    


# In[ ]:





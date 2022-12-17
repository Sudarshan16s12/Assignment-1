#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python program to get the Fibonacci series between 0 to 50.
start = int(input("enter the start num:"))
end = int(input("enter the end num:"))
x,y=0,1
while y<end:
    print(y)
    x,y = y,x+y


# In[13]:


#Write a Python program that accepts a word from the user and reverse it.
x = input("enter the word to reverse:")
for i in range(len(x)-1,-1,-1):
    print(x[i], end=" ")


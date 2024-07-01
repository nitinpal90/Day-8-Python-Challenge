#!/usr/bin/env python
# coding: utf-8

# # Day-8 Python Challenge

# # List in Python

# # Creating a List

# In[1]:


mybook = ["Appple", "Mango", "Banana"]
print(mybook)
print(type(mybook))


# In[2]:


a = ["BCA", "MBA", "BCA", "BTECH", "MBA"] ## List is allowed to Duplicates 
print(a)


# # Data Types in List

# In[4]:


list1 = ["Apple", "Books"] ## List is allow all the data types 
list2 = [2,3,4,5]
list3 = [1.2, 2.3]
list4 = [True, False]
print(list1)
print(list2)
print(list3)
print(list4)


# # Length in List

# In[5]:


a = [15,8,9,3,4,6,7,8,9,25]
print(len(a))


# # Access Items in List 

# In[7]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
print(a[14])


# # Slicing of List

# In[9]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
print(a[5:10])


# In[10]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
print(a[5:10:2])


# # Change Items in lIst

# In[12]:


a = ["Apple", "Mango"]
a[1] = "Cheery"
print(a)


# In[13]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
a[5] = "BCA"
print(a)


# # Change a range of items values

# In[14]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
a[5:8] = ["BCA", "MBA", "BBA"]
print(a)


# # Append Function use to add value

# In[15]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6]
a.append(1)
print(a)


# # Remove Function

# In[18]:


a = ["Apple", "Mango"]
a.remove("Mango")
print(a)


# # Reverse Function

# In[19]:


a = [1,2,3,4,5,6,7,8,4,5,6,4,43,4,5,63,5,6, "Apple","Mango"]
a.reverse()
print(a)


# # Find the sum of a list

# In[23]:


a = [1,2,3,6,7,19,40,87,89]
print(len(a))
l=0
for i in range(9):
    l = l+a[i]
    i = i+1
print("The sum of list is:",l)


# # Multiply all the numbers of a list

# In[28]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = 1
for i in a:
    b *= i

print("The product of all the numbers in the list is:", b)


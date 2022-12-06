#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:




def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [10, 7, 2, 5, 9]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


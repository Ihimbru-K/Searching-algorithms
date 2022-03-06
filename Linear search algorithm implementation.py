# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:54:17 2022

@author: mon pc
"""


#linear search algorithm in python
def Lin_Search(lis, n, key): #a linear search function is defined which takes 3 parameters; our list, the length of the list,n and the key which is the element we are looking for 
    for i in range(0, n): 
        if lis[i] == key: #if element at a given index is the given element we're looking for in our list,
            return i #we return the index of element
    else:
            return -1  # else return -1 to show that the element we are looking for is not present in the list

lis = [1, 2, 3, 4, 5, 6, 7, 8]
key = 7
n = len(lis)


result = Lin_Search(lis, n, key)
if result == -1:
    print("element is not found")
else:
    print("element is at index:" ,result)
    
    

# Time complexity of linear search algorithm -
# o Base Case - O(1)
# o Average Case - O(n)
# o Worst Case -O(n) 
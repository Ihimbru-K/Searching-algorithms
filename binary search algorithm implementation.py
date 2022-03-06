# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:17:39 2022

@author: mon pc
"""


#binary search algorithm
def Bin_Search(list1, n):
    low =  0
    high = len(list1)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        
        if list1[mid] > n:
            high = mid - 1
            
        elif list1[mid] < n:
             low = mid + 1
        else:
            return mid
    return -1

list1 = [10, 20, 30, 40, 50]
n = 50

result = Bin_Search(list1, n)

if result == -1:
    print("element is not found in list")
else:
    print("element is found in index", str(result))

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:26:50 2022

@author: USER
"""

import random
import os.path

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n - 1)
    
def RandomArray(size):
    array = []
    min = 0
    max = 1000
    for i in range (0, size):
        num = random.randint(min, max)
        array.append(num)
    return array

def InsertionSort(array, start, end):
    for i in range(start, end, 1):
        key = array[i]
        j = i - 1
        while(key > array[j] and j >= 0):
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def MergeSort(array, start, end):
    if (start < end):
        mid = (start + end)//2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    L = [0]*(n1)
    R = [0]*(n2)
    
    for i in range(0, n1, 1):
        L[i] = array[p + i]
    
    for j in range(0, n2, 1):
        R[j] = array[q + j + 1]
    
    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if (L[i] < R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
        
def HybridMergeSort(array, start, end):
    dif = end - start
    if (start < end and dif > 43):
        mid = (start + end)//2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    else:
        InsertionSort(array, start, end)

def ShuffleArray(array, start, end):
    min = start
    max = end
    A = []
    for i in range (0, len(array), 1):
        x = random.randint(min, (max - 1))
        if (checkArray(A, x)):
            temp1 = array[x]
            array[x] = array[i]
            array[i] = temp1
            A.append(x)
        else:
            i -= 1
    return array
            
def checkArray(array, x):
    for i in range(0,len(array),1):
        if (array[i] == x):
            return False
    return True

def readDataFromFile(path):
    if (os.path.exists(path)):
        fileVariable = open(path, 'r')
        lines = fileVariable.read()
        numbers = []
        arr = lines.split()
        fileVariable.close()
        for n in arr:
            num = n
            numbers.append(num)
        return numbers
    else:
        return None

def storeIntoTheFile (arr,path):
    f = open (file = path, mode = 'w')
    for i in arr:
        f.write(str(i) + "\n")
        
def BubbleSort(array, start, end):
    i = len(array)
    Sorted = False
    while ((i > 1) and not(Sorted)):
        Sorted = True
        for j in range(start, end, 1):
            if (array[j-1] < array[j]):
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
                Sorted = False
        i -= 1
    return array

def Minimum(Arr, starting, ending):
    smallest = 10000000
    idx = 0
    for i in range(starting, ending, 1):
        if(smallest > Arr[i]):
            smallest = Arr[i]
            idx = i
    return idx

def SelectionSort(array, start, end):
    for i in range (start, end, 1):
        smallest_idx = Minimum(array, i, end)
        temp1 = array[smallest_idx]
        array[smallest_idx] = array[i]
        array[i] = temp1
    return array    
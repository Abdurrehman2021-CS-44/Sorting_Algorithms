# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:18:21 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "SortedMergeSort.csv"
    n = 30000
    array = funcs.RandomArray(n)
    
    start_time = time.time()
    funcs.MergeSort(array, 0, n-1)
    end_time = time.time()
    
    print (array)

    runtime = end_time - start_time

    print("Runtime of Merge Sorting at ",n," is ",runtime," second")
    funcs.storeIntoTheFile(array, path)
    
if __name__ == "__main__":
    main()
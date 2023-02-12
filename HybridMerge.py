# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:03:40 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "SortedHybridSort.csv"
    n = 30000
    array = funcs.RandomArray(n)
    
    start_time = time.time()
    funcs.HybridMergeSort(array, 0, n)
    end_time = time.time()
    
    print (array)

    runtime = end_time - start_time

    print("Runtime of Hybrid Merge Sorting at ",n," is ",runtime," second")
    funcs.storeIntoTheFile(array, path)
    
if __name__ == "__main__":
    main()
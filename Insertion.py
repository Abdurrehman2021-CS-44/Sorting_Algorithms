# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:40:12 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "SortedInsertionSort.csv"
    n = 30
    array = funcs.RandomArray(n)
    
    start_time = time.time()
    arraySort = funcs.InsertionSort(array, 0, n)
    end_time = time.time()

    runtime = end_time - start_time

    print(arraySort)
    print("Runtime of Insertion Sorting at ",n," is ",runtime," second")
    funcs.storeIntoTheFile(arraySort, path)
    
if __name__ == "__main__":
    main()
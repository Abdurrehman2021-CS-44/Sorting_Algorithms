# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:18:08 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "SortedSelectionSort.csv"
    n = 30000
    array = funcs.RandomArray(n)
    
    start_time = time.time()
    arraySort = funcs.SelectionSort(array, 0, n)
    end_time = time.time()

    runtime = end_time - start_time

    print(arraySort)
    print("Runtime of Bubble Sorting at ",n," is ",runtime," second")
    funcs.storeIntoTheFile(arraySort, path)
    
if __name__ == "__main__":
    main()
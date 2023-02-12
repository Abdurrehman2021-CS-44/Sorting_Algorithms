# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:54:11 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "SortedBubbleSort.csv"
    n = 30
    array = funcs.RandomArray(n)
    
    start_time = time.time()
    arraySort = funcs.BubbleSort(array, 1, len(array))
    end_time = time.time()

    runtime = end_time - start_time

    print(arraySort)
    print("Runtime of Bubble Sorting at ",n," is ",runtime," second")
    funcs.storeIntoTheFile(arraySort, path)
    
if __name__ == "__main__":
    main()
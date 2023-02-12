# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:44:40 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    valuesPath = "Nvalues.txt"
    timePath = "RunTime.csv"
    array = funcs.readDataFromFile(valuesPath)
    
    insertionTimeArray = []
    mergeTimeArray = []
    hybridMergeTimeArray = []
    bubbleTimeArray = []
    selectionTimeArray = []
    
    for i in array:
        i = int(i)
        
        Array_1 = funcs.RandomArray(i)
        start_time_insertion = time.time()
        insertionArraySort = funcs.InsertionSort(Array_1, 0, i)
        end_time_insertion = time.time()
        
        Array_2 = funcs.RandomArray(i)
        start_time_merge = time.time()
        funcs.MergeSort(Array_2, 0, i - 1)
        end_time_merge = time.time()
        
        Array_3 = funcs.RandomArray(i)
        start_time_hybrid_merge = time.time()
        funcs.HybridMergeSort(Array_3, 0, i - 1)
        end_time_hybrid_merge = time.time()
        
        Array_4 = funcs.RandomArray(i)
        start_time_bubble = time.time()
        bubbleArraySort = funcs.BubbleSort(Array_4, 1, i)
        end_time_bubble = time.time()
        
        Array_5 = funcs.RandomArray(i)
        start_time_selection = time.time()
        selectionArraySort = funcs.SelectionSort(Array_5, 0, i)
        end_time_selection = time.time()

        runtime_insertion = end_time_insertion - start_time_insertion
        runtime_merge = end_time_merge - start_time_merge
        runtime_hybrid_merge = end_time_hybrid_merge - start_time_hybrid_merge
        runtime_bubble = end_time_bubble - start_time_bubble
        runtime_selection = end_time_selection - start_time_selection
        
        insertionTimeArray.append(runtime_insertion)
        mergeTimeArray.append(runtime_merge)
        hybridMergeTimeArray.append(runtime_hybrid_merge)
        bubbleTimeArray.append(runtime_bubble)
        selectionTimeArray.append(runtime_selection)
        
        print("Runtime of Insertion Sorting at ",i," is ",runtime_insertion," second")
        print("Runtime of Merge Sorting at ",i," is ",runtime_merge," second")
        print("Runtime of Hybrid Merge Sorting at ",i," is ",runtime_hybrid_merge," second")
        print("Runtime of Bubble Sorting at ",i," is ",runtime_bubble," second")
        print("Runtime of Selection Sorting at ",i," is ",runtime_selection," second")
    
    f = open (file = timePath, mode = 'w')
    for i in range(0,len(array),1):
        f.write(str(insertionTimeArray[i]) + "," + str(mergeTimeArray[i]) + "," + str(hybridMergeTimeArray[i])+ "," + str(selectionTimeArray[i]) + "," + str(bubbleTimeArray[i]) + "\n")
    
if __name__ == "__main__":
    main()
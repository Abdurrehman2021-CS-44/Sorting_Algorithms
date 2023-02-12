# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:11:32 2022

@author: USER
"""

import funcs
import time

# Defining Main Function
def main():
    path = "words.txt"
    array_1 = funcs.readDataFromFile(path)
    array_2 = funcs.readDataFromFile(path)

    start_time_insertion_1 = time.time()
    insertion_sort_array_1 = funcs.InsertionSort(array_1, 0, len(array_1))
    end_time_insertion_1 = time.time()
    
    start_time_merge_1 = time.time()
    funcs.MergeSort(array_2, 0, len(array_2)-1)
    end_time_merge_1 = time.time()
    
    runtime_insertion_1 = end_time_insertion_1 - start_time_insertion_1
    runtime_merge_1 = end_time_merge_1 - start_time_merge_1

    print("Runtime of Insertion Sorting " , " is ",runtime_insertion_1," second.")
    print("Runtime of  Merge Sorting " , " is ",runtime_merge_1," second.")
    
    shuffle_array_1 = funcs.ShuffleArray(array_1, 0, len(array_1))
    shuffle_array_2 = funcs.ShuffleArray(array_1, 0, len(array_1))
    
    start_time_insertion_2 = time.time()
    insertion_sort_array_2 = funcs.InsertionSort(shuffle_array_1, 0, len(shuffle_array_1))
    end_time_insertion_2 = time.time()
    
    start_time_merge_2 = time.time()
    funcs.MergeSort(shuffle_array_2, 0, len(shuffle_array_2)-1)
    end_time_merge_2 = time.time()

    runtime_insertion_2 = end_time_insertion_2 - start_time_insertion_2
    runtime_merge_2 = end_time_merge_2 - start_time_merge_2
    
    print("Runtime of Insertion Sorting " , " is ",runtime_insertion_2," second.")
    print("Runtime of Merge Sorting " , " is ",runtime_merge_2," second.")

if __name__ == "__main__":
    main()
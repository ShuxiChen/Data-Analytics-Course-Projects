import random
import time
import pandas as pd
import numpy as np

# bubble sort
def bubble_sort(nums):
    start_time = time.time()
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    end_time = time.time()
    return end_time - start_time

# selection sort
def selection_sort(nums):
    start_time = time.time()
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
    end_time = time.time()
    return end_time - start_time
            

# insertion sort
def insertion_sort(nums):
    start_time = time.time()
    for i in range(1, len(nums)):
        j = i
        while nums[j - 1] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    end_time = time.time()
    return end_time - start_time


# quick sort
def quick_sort(nums, left, right):
    start_time = time.time()
    
    if left < right:
        partition_pos = partition(nums, left, right)
        quick_sort(nums, left, partition_pos - 1)
        quick_sort(nums, partition_pos + 1, right)
        
    end_time = time.time()
    return end_time - start_time
        

def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]
    
    while i < j:
        
        while i < right and nums[i] < pivot:
            i += 1
        
        while j > left and nums[j] >= pivot:
            j -= 1
        
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    
    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]
    
    return i


# heap sort     
def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def siftDown(nums, i, upper):
    
    while(True):
        l, r = i*2+1, i*2+2
       
        if max(l, r) < upper:
            
            if nums[i] >= max(nums[l], nums[r]):
                break
            elif nums[l] > nums[r]:
                swap(nums, i, l)
                i = l
            else:
                swap(nums, i, r)
                i = r
        elif l <upper:
            
            if nums[l] > nums[i]:
                swap(nums, i, l)
                i = l
            else:
                break
        
        elif r < upper:
           
            if nums[r] > nums[i]:
                swap(nums, i, r)
                i = r
            else: 
                break
        
        else:
            break

def heap_sort(nums):  
    start_time = time.time()
    
    for j in range((len(nums) - 2) // 2, -1, -1):
        siftDown(nums, j, len(nums))
    
    for end in range(len(nums) - 1, 0, -1):
        swap(nums, 0, end)
        siftDown(nums, 0, end)
    
    end_time = time.time()
    return end_time - start_time
                 

# input sizes
n_values = [1000, 5000, 10000, 15000, 20000, 50000]

sorting_functions = [bubble_sort, selection_sort, insertion_sort, quick_sort, heap_sort]

# calculate mean sorting times
def calculate_mean_sorting_times(n_values, sorting_functions):
    mean_times = {}
    for n in n_values:
        times = {}
        for sorting_func in sorting_functions:
            sorting_times = []
            iterations = 25
            for _ in range(iterations):
                lst = [random.randint(-1000, 1000) for _ in range(n)]
                time_taken = sorting_func(lst.copy())
                sorting_times.append(time_taken)
            mean_time = np.mean(sorting_times)
            times[sorting_func] = mean_time
        mean_times[n] = times
    return mean_times



if __name__ == "__main__":

    # Calculate mean sorting times for different input sizes and sorting algorithms
    mean_sorting_times = calculate_mean_sorting_times(n_values, sorting_functions)

    # Convert the mean_sorting_times dictionary to a DataFrame
    df = pd.DataFrame(mean_sorting_times)

# df.to_excel("filename.xlsx", index = True)
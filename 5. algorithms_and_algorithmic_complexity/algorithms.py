
"""
Algorithms Module
=================

---------------------------------------------------------------------------
-------------------------Sorting Algorithms--------------------------------
---------------------------------------------------------------------------

This module contains multiple sorting algorithms—each suited for different
scenarios depending on data size, structure, and performance requirements.
Use the guidelines below to select the appropriate algorithm.

Algorithms Included
-------------------
1. Insertion Sort
2. Bubble Sort
3. Merge Sort
4. Quick Sort

When to Use Each Algorithm
--------------------------

1. Insertion Sort
   - Best for very small datasets (typically fewer than 50 elements).
   - Performs extremely well on *nearly sorted* lists.
   - Simple, stable, and predictable.
   - Time Complexity:
       Best: O(n)
       Average/Worst: O(n^2)
   - Use when: you want a simple, efficient method for small or almost-sorted lists.

2. Bubble Sort
   - Educational algorithm, rarely used in production.
   - Useful when teaching sorting fundamentals or when you need a simple algorithm
     with minimal code complexity.
   - Performs well only on very small datasets or when the list is already almost sorted.
   - Time Complexity: O(n^2)
   - Use when: simplicity matters more than performance.

3. Merge Sort
   - Best choice for large datasets requiring guaranteed performance.
   - Very stable and consistent: always O(n log n) regardless of input order.
   - Not in-place (uses additional memory).
   - Excellent for sorting linked lists or any structure where random access is expensive.
   - Use when: you need stable, predictable performance on large datasets.

4. Quick Sort
   - Typically the fastest in practice for large in-memory lists.
   - Average-case: O(n log n)
   - Worst-case: O(n^2) if the pivot choice is poor (mitigated using randomized or median pivot).
   - In-place and memory-efficient.
   - Use when: you want high performance on large lists and can accept worst-case risk.

General Recommendations
-----------------------
- For **large datasets**: prefer Merge Sort or Quick Sort.
- For **small datasets**: use Insertion Sort.
- For **mostly sorted data**: Insertion Sort performs best.
- For **teaching or demonstration**: Bubble Sort is simplest.
- For **production-quality stability**: Merge Sort.
- For **speed with low memory usage**: Quick Sort.


---------------------------------------------------------------------------
-------------------------Searching Algorithms------------------------------
---------------------------------------------------------------------------

The following searching algorithms are included:
1. Linear Search
2. Binary Search

Choosing a Searching Algorithm
------------------------------

- Linear Search:
    - Works on **any** list (sorted or unsorted).
    - Simple but slow for large datasets.
    - Time Complexity: O(n).

- Binary Search:
    - Requires the list to be **sorted**.
    - Very fast for large datasets.
    - Time Complexity: O(log n).
    - Use after applying a sorting algorithm.

General Searching Recommendations
---------------------------------
- Use **Linear Search** for unsorted or very small lists.
- Use **Binary Search** for large, sorted datasets.
- Combine sorting + binary search when:
    - Many searches will be performed on the same dataset.
    - Sorting once and searching frequently gives efficiency.

---------------------------------------------------------------------------
This module therefore serves both as a practical toolkit and a learning
resource for understanding foundational algorithmic strategies

"""


#=================================================================================================
#                                      SEARCHING ALGORITHMS
#=================================================================================================

#-------------------------------------ITERATIVE BINARY SEARCH----------------------------------------------------------------------

def iterative_binary_search(iterate, element):
    """
    This is an iterative binary search algorithm that searches for the index of an item in a iterate that is eg a list

    The parameters are as follows:
    -----
    iterate: list, tuple etc
    element: This is the item whose index we are looking for

    The expected output
    -----
    The expected out is the index of the elemnt that we are searching for int the list
    """

    low = 0 
    high = len(iterate) - 1

    while low <= high:
        mid = (low + high)// 2
        if iterate[mid] == element:
            return mid
        elif iterate[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

#----------------------------------------RCURSIVE BINARY SEARCH-----------------------------------------------------------------

def recursive_binary_search(iterate, element, low, high):
    """
    This is a recursive binary search algorithm that searches for the index of the element we are looking for in an iterate

    The parameters are as follows:
    -----
    iterate: eg a list
    element: The item we are looking for
    low: The first index of the iterate which when starting is always 0
    high: The last index of the iterate which is len(itetate) - 1

    The expected output
    ------
    The expected output is the index of the element we are looking for
    """

    if low > high:
        return False

    mid = (low + high) // 2

    if iterate[mid] == element:
        return mid
    elif iterate[mid] < element:
        return recursive_binary_search(iterate, element, mid + 1, high)
    else:
        return recursive_binary_search(iterate, element, low, mid - 1)

    
#------------------------------------------------LINEAR SEARCH ALGO----------------------------------------------------------------


def linear_search(items, target):
    """
    Perform a linear search to find the index of a target value within a list.

    This function iterates through the list from the first element to the last,
    comparing each element to the target. If the target is found, the function
    returns its index. If the target is not present in the list, the function
    returns False.

    Parameters
    ----------
    items : list
        The list of elements to search through.
    target : any
        The value to search for within the list.

    Returns
    -------
    int
        The index of the target element if found.
    bool
        False if the target element is not found.
    """
    for i in range(len(items)):
        if items[i] == target:
            return i
    return False

        
#=================================================================================================
#                                      SORTING ALGORITHMS
#=================================================================================================

#--------------------------------------BUBBLE SORT ALGORITHM---------------------------------
def bubbles(iterate):
    """
    Sort a list using a modified bubble sort algorithm.

    This implementation repeatedly iterates through the list, comparing
    adjacent elements and swapping them when they are out of order.
    After each full pass, the next largest element is guaranteed to be
    correctly positioned at the end of the list. The algorithm reduces
    the comparison range after each iteration and stops early if no
    swaps occur, indicating the list is already sorted.

    Parameters
    ----------
    iterate : list
        The list of comparable elements to be sorted.

    Returns
    -------
    list
        The sorted version of the input list.
    """
    index = len(iterate) - 1
    sorted_flag = False

    while not sorted_flag:
        sorted_flag = True  # Assume sorted until a swap proves otherwise

        for i in range(index):
            if iterate[i] > iterate[i + 1]:
                sorted_flag = False
                iterate[i], iterate[i + 1] = iterate[i + 1], iterate[i]

        index -= 1  # Reduce comparison range after each full pass

    return iterate


#--------------------------------------INSERTION SORT ALGO---------------------------------


def insertion_sort_alo(iterate):
    """
    Sort a list in ascending order using the insertion sort algorithm.

    The algorithm builds the sorted list one element at a time. For each
    element, it shifts larger elements to the right until the correct
    position is found, and then inserts the element there.

    Parameters
    ----------
    iterate : list
        The list of comparable elements to be sorted.

    Returns
    -------
    list
        The list sorted in ascending order.
    """
    for i in range(1, len(iterate)):
        value_to_sort = iterate[i]
        j = i

        while j > 0 and iterate[j - 1] > value_to_sort:
            iterate[j] = iterate[j - 1]
            j -= 1

        iterate[j] = value_to_sort

    return iterate


#--------------------------------------BMERGE SORT ALGO---------------------------------


def merge_sort(arr):
    """
    Sort a list using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that recursively divides
    the list into halves, sorts each half, and then merges the two sorted
    halves into a fully sorted list.

    Parameters
    ----------
    arr : list
        The list of comparable elements to be sorted.

    Returns
    -------
    list
        A new list containing all elements from the input list in
        ascending order.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    This function takes two individually sorted lists and merges them by
    repeatedly selecting the smallest available element from either list.

    Parameters
    ----------
    left : list
        The first sorted list.
    right : list
        The second sorted list.

    Returns
    -------
    list
        A merged and sorted list containing all elements from both inputs.
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


#--------------------------------------BQUICK SORT ALGO---------------------------------

def quick_sort(arr, low, high):
    """
    Sort a list in ascending order using the quick sort algorithm.

    Quick sort is a divide-and-conquer algorithm that selects a pivot,
    partitions the list around the pivot so that smaller elements are on
    the left and larger elements are on the right, and then recursively
    sorts the partitions.

    Parameters
    ----------
    arr : list
        The list of comparable elements to be sorted.
    low : int
        The starting index of the portion of the list to sort
        (typically 0).
    high : int
        The ending index of the portion of the list to sort
        (typically len(arr) - 1).

    Returns
    -------
    None
        The function sorts the list in place.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    """
    Partition the list around a pivot element.

    The pivot is chosen as the last element of the list segment. All
    elements smaller than or equal to the pivot are moved to the left,
    and elements greater than the pivot remain on the right. The pivot is
    then placed in its correct sorted position.

    Parameters
    ----------
    arr : list
        The list being partitioned.
    low : int
        The starting index of the segment to partition.
    high : int
        The ending index of the segment; this is where the pivot is read.

    Returns
    -------
    int
        The index where the pivot is finally placed.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


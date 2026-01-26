#!python

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    running time: O(n + m) - n/m are lengths of items1 and items2 bc we iterate through each item exactly once
    memory usage: O(n + m) bc we create a new list to hold all items"""
    merged = []
    i, j = 0, 0
    # repeat until one list is empty
    while i < len(items1) and j < len(items2):
        # find min item in both lists and append to new list
        if items1[i] <= items2[j]:
            merged.append(items1[i])
            i += 1
        else:
            merged.append(items2[j])
            j += 1
    # append remaining items in non-empty list to new list
    merged.extend(items1[i:])
    merged.extend(items2[j:])
    return merged

    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    running time: O(n^2) bc we use an O(n^2) iterative sorting algorithm (insertion sort) on each half, and O(n) to merge
    memory usage: O(n) bc we create new lists for each half and the merged result"""
    # base case: list is already sorted if it has 0 or 1 items
    if len(items) <= 1:
        return items
    # split items list into approx. equal halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    # sprt each half using an iterative sorting algo (insertion sort)
    from sorting_iterative import insertion_sort
    insertion_sort(left)
    insertion_sort(right)
    # merge sorted halves into one list in sorted order
    merged = merge(left, right)
    # copy merged items back into original list to sort in place
    items[:] = merged
    return items

    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    
    running time: O(n log n) bc we split the list in half log n times and merge takes O(n) time at each level.
    memory usage: O(n) bc we create new lists for merging at each level, plus O(log n) for recursive call stack"""
    # check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # split items list into approx. equal halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    # sort each half by recursively calling merge sort
    merge_sort(left)
    merge_sort(right)
    # merge sorted halves into one list in sorted order
    merged = merge(left, right)
    # copy merged items back into original list to sort in place
    items[:] = merged
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

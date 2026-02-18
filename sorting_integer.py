#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.

    running time: O(n + k) where n is length of numbers and k is range (max - min)
    memory usage: O(k) for the counts array where k is range of input values."""
    # check if list is empty or has one item (already sorted)
    if len(numbers) <= 1:
        return numbers
    # find range of given numbers (min and max values)
    min_val = min(numbers)
    max_val = max(numbers)
    # create list of counts with slot for each num in input range
    k = max_val - min_val + 1
    counts = [0] * k
    # loop over given numbers and increment each num's count
    for num in numbers:
        counts[num - min_val] += 1
    # loop over counts and copy that many nums into original list 
    index = 0
    for i in range(k):
        for _ in range(counts[i]):
            numbers[index] = i + min_val
            index += 1
    return numbers

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.

    running time: O(n + k) average case where n is length and k is num_buckets,
                  O(n^2) worst case if all numbers fall into one bucket.
    memory usage: O(n + k) for storing numbers across k buckets."""
    # check if list is empty or has one item (already sorted)
    if len(numbers) <= 1:
        return numbers
    # find range of given numbers (min and max values)
    min_val = min(numbers)
    max_val = max(numbers)
    # handle edge case where all nums are the same
    if min_val == max_val:
        return numbers
    # create list of buckets to store nums in subranges of input range
    buckets = [[] for _ in range(num_buckets)]
    # calculate the range each bucket covers
    bucket_range = (max_val - min_val + 1) / num_buckets
    # loop over given nums and place each item in appropriate bucket
    for num in numbers:
        # calculate bucket index (ensure last element goes in last bucket)
        bucket_index = int((num - min_val) / bucket_range)
        if bucket_index == num_buckets:
            bucket_index -= 1
        buckets[bucket_index].append(num)
    # sort each bucket using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)
    # loop over buckets and copy nums back into original list (mutate in place)
    index = 0
    for bucket in buckets:
        for num in bucket:
            numbers[index] = num
            index += 1
    return numbers

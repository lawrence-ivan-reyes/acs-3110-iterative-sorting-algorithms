#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    running time: O(n) - must check all adjacent pairs in the worst case.
    memory usage: O(1) - only uses a constant amount of extra variables."""
    # checking that all adjacent items are in order, return early if not
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    running time: O(n^2) worst/avg case, O(n) best case if already sorted.
    memory usage: O(1) - sorts in place using only constant extra space."""
    n = len(items)
    # repeat until all items are in sorted order
    for i in range(n):
        swapped = False
        # swap adjacent items that are out of order
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # if no swaps occurred, list is already sorted
        if not swapped:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    running time: O(n^2) always - must scan unsorted portion for each position.
    memory usage: O(1) - sorts in place using only constant extra space."""
    n = len(items)
    # repeat until all items are in sorted order
    for i in range(n):
        # find min item in unsorted items
        min_index = i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        # swap w/ first unsorted item
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    running time: O(n^2) worst/avg case, O(n) best case if already sorted.
    memory usage: O(1) - sorts in place using only constant extra space."""
    # repeat until all items are in sorted order
    for i in range(1, len(items)):
        # take first unsorted item
        current = items[i]
        j = i - 1
        # insert in sorted order in front of items
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current

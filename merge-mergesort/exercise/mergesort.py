from heapq import merge

def merge_sort2(m):
    """Sort list, using two part merge sort"""
    if len(m) <= 1:
        return m

    # Determine the pivot point
    middle = len(m) // 2

    # Split the list at the pivot
<<<<<<< HEAD
    right = m[middle:]
    left = m[:middle]
=======
    left = m[:middle]
    right = m[middle:]
>>>>>>> master

    # Sort recursively
    right = merge_sort2(right)
    left = merge_sort2(left)

    # Merge and return
    return list(merge(right, left))

def merge_sort4(m):
    """Sort list, using four part merge sort"""
    if len(m) <= 4:
        return sorted(m)

    # Determine the pivot point
    middle = len(m) // 2
    leftMiddle = middle // 2
    rightMiddle = middle + leftMiddle

    # Split the list at the pivots
    first = m[:leftMiddle]
    second = m[leftMiddle:middle]
    third = m[middle:rightMiddle]
<<<<<<< HEAD
    fourth = m[rightMiddle:]
=======
    last = m[rightMiddle:]
>>>>>>> master

    # Sort recursively
    first = merge_sort4(first)
    second = merge_sort4(second)
    third = merge_sort4(third)
<<<<<<< HEAD
    fourth = merge_sort4(fourth)

    # Merge and return
    return list(merge(first,second, third, fourth))
=======
    last = merge_sort4(last)

    # Merge and return
    return list(merge(first, second, third, last))
>>>>>>> master
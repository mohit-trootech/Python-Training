"""
 Method that perform the merge operation with two lists.
"""


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result


""" 
 Mergesort algorithm recursive implementation.
"""


def mergesort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = mergesort(l[:middle])
        right = mergesort(l[middle:])

        together = merge(left, right)
        print('Merged ', together)
        return together


"""
 Sample example of execution :
"""
numbers = [2, 0, 9, 6, 4, 3, 5, 8, 1, 7]

ordered = mergesort(numbers)

print(ordered)

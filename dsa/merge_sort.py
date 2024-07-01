"""
 Method that perform the merge operation with two lists.
"""

from Python_Learning.time_complexity import check_complexity


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
        return together


@check_complexity
def main():
    """
    Sample example of execution :
    """
    numbers = [2, 0, 9, 6, 4, 3, 5, 8, 1, 7]

    ordered = mergesort(numbers)

    print(ordered)


main()
print(
    "Average Time: {:.10f}".format(
        sum([0.000069141 + 0.000077486 + 0.000066519 + 0.000066519 + 0.000063419]) / 5,
    )
)

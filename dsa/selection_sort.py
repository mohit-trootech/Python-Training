"""Python Selection Sort Example"""

unsorted_list = [41, 1, 51235, 54, 52, 626, 126, 16, 1, 61, 6, 163, 136, 1, 13, 1]


def selection_sorting(lst):
    print(f"Unsorted List = {lst}")
    for i in range(1, len(lst)):
        print(lst)
        for j in range(i):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(f"Sorted List = {lst}")


selection_sorting(unsorted_list)

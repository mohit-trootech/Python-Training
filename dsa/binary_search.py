# Binary Search


def binary_search(l, start, end, mid, find):
    if l[mid] > find:
        print(mid)
        binary_search(start, mid, (start + end) // 2, find)
    elif l[mid] < find:
        print(mid)
        binary_search(start, mid, (start + end) // 2, find)
    elif l[mid] == find:
        return f"element found on Index {mid}"


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 67, 8, 9]
    print(binary_search(lst, 0, len(lst) - 1, len(lst) // 2, 67))

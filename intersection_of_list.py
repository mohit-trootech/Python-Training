# python program to find intersection of lists


def intersection_lists(*args):
    result_list = args[0]
    for i in range(1, len(args)):
        result_list = [i for i in args[i] if i in result_list]
    return sorted(result_list)


if __name__ == "__main__":
    print(intersection_lists([2, 3, 4, 5], [2, 3, 4], [4, 3, 5, 6]))

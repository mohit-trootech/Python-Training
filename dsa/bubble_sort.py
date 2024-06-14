def bubble_sorting(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


print(bubble_sorting([789174, 153, 5235, 16, 16, 1, 61, 46412, 46, 23, 22, 1]))

from divisible_by_n import divisible


def greater_args(lst, num):
    """Python Program to Return True if all list items are divisible by number"""
    print(all(lst) % 790 == 0)
    if any(i % num == 0 for i in lst):
        print("True")


greater_args([79, 10], 2)

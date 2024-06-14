# Python program to find the highest common factor
from divisible_by_n import divisible
from prime_number_module import is_prime
from intersection_of_list import intersection_lists

def hcf(*args):
    hcf_dict = {}
    for i in args:
        hcf_dict[i] = []
        if is_prime(i):
            hcf_dict[i].append(i)
        else:
            temp = i
            j = 2
            while j < temp:
                if divisible(i, j):
                    i = int(i)//int(j)
                    hcf_dict[temp].append(j)
                else:
                    j += 1
    hcf_dict.setdefault(f"HCF of {list(args)}", intersection_lists(*list(hcf_dict.values())))
    return hcf_dict



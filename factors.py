from divisible_by_n import divisible
from prime_number_module import is_prime


def factors(args):
    factors_list = []
    if is_prime(args):
        factors_list.append(args)
    else:
        i = 2
        temp_variable = args
        if temp_variable != 0:
            while i < args:
                if divisible(temp_variable, i):
                    temp_variable = int(temp_variable) // int(i)
                    factors_list.append(i)
                else:
                    i += 1
    return factors_list


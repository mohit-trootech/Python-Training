# # from math import pi
# #
# # import numpy as np
# # from matplotlib import pyplot as plt
# #
# # u = 1.  # x-position of the center
# # v = 0.5  # y-position of the center
# # a = 2.  # radius on the x-axis
# # b = 1.5  # radius on the y-axis
# #
# # t = np.linspace(0, 2 * pi, 100)
# # plt.plot(u + a * np.cos(t), v + b * np.sin(t))
# # plt.grid(color='black', linestyle='--')
# import sys
#
# print(hasattr(sys, 'set_int_max_str_digits'))
# delattr(sys, 'set_int_max_str_digits')
# print(hasattr(sys, 'set_int_max_str_digits'))
# print(sys.get_int_max_str_digits())
# setattr(sys, 'set_int_max_str_digits', 5000)
# print(hasattr(sys, 'set_int_max_str_digits'))
# print(sys.set_int_max_str_digits)

def __eq__(a, b):
    return a.__eq__(b)


print(5 == 5)

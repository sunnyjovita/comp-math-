import math
import numpy as np

#  number 1
# def Taylor_ln(x, h):
# #     # x<1
#     x = x-1
#     ans = 0
#     for i in range(1, h+1):
# #         # for even number
#         if(i%2 == 0):
#             ans = ans - (x**i)/i
# #         #     for odd number
#         elif(i%2 == 1):
#             ans = ans + (x**i)/i
#     return ans
#
# Approximal_value = Taylor_ln(1.5, 10)
# print("Approxima Value: %f" %(Approximal_value))
# True_value = np.log(1.5)
# print("True Value: %f" %(True_value))
# True_error = True_value - Approximal_value
# print("True Error: %f" %(True_error))
#
# print("==================")

def Taylor2_ln(x,h):
    # x<1
    x = x-1
    ans = 0
    for i in range(1, 21):
        print(i)
        # for even number
        if (i % 2 == 0):
            ans = ans - (x ** i) / i
        #     for odd number
        elif (i % 2 == 1):
            ans = ans + (x ** i) / i
        return ans

#         True_value = np.log(1.5)
#         print("True Value: %f" %(True_value))
#         True_error =
#         Relative_True_error = Tr

# print(Taylor2_ln(1.5,20))
print(Taylor2_ln(1.5, 20))

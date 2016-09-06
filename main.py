from FileReadLib import get_array
from TwoSumLib import two_sum_dict

import numpy as np

filename = "algo1-programming_prob-2sum"
a = get_array(filename)


# Prepare to find 2-sums by sorting the array
a.sort()

targets = range(-10000,10001)
found_2sum = two_sum_dict(a, targets)

np.save("output", found_2sum)

print("all done.")
from FileReadLib import get_array

import numpy as np

filename = "algo1-programming_prob-2sum"
a = get_array(filename)

def two_sum(ar, target):
    # Determine whether there are two distinct elements in array which sum to target

    n = len(ar)
    sum_found = False
    done = False
    i1 = 0

    while not sum_found and not done:
        p1 = ar[i1]
        complement = target - p1
        if p1 != complement:
            if is_present(ar[p1+1:], complement):
                sum_found = True

        if p1 > (target/2):
            done = True

        i1 += 1


    return sum_found

def is_present(ar, value):
    # Use binary search to check whether given value is present in (sorted) array
    presence = False
    n = len(ar)

    if value >= ar[0] and value <= ar[n-1]:
        middle_value = ar[int(n / 2)]
        if value > middle_value:
            presence = is_present(ar[int(n / 2) + 1:], value)
        elif value < middle_value:
            presence = is_present(ar[:int(n / 2)], value)
        else:
            presence = True


    return presence

# Prepare to find 2-sums by sorting the array
a.sort()

targets = range(-10000,10000)
nTargets = len(targets)
distinct_2sum = nTargets * [False]

for iTarget in range(nTargets):
    if iTarget%100==0:
        print(iTarget)
    distinct_2sum[iTarget] = two_sum(a, targets[iTarget])



print("all done.")
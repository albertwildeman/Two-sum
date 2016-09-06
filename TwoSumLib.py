
def two_sum_dict(a, targets):

    # convert list to dictionary
    d = {x: True for x in a}

    sums_found = len(targets) * [False]

    for iTarget, target in enumerate(targets):

        print("Working on target # " + str(iTarget))
        # done = False
        # i = 0

        for x in a:
            if (target - x) in d:
                if 2*x != target:
                    sums_found[iTarget] = True

    return sums_found


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

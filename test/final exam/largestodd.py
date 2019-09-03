def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
     largest_odd_times([2,2,4,4]) returns None
     largest_odd_times([3,9,5,3,5,3]) returns 9
           Returns the largest element of L that occurs an odd number
           of times in L. If no such element exists, returns None """
    # Your code here
    odd = 0
    numkey = 0
    dict = {}
    for c in L:
        if c not in dict.keys():
            dict[c] = 1
        else:
            dict[c] += 1
    for k, v in dict.items():
        if v % 2 != 0 and k > numkey:
            odd = v
            numkey = k

    if odd == 0:
        return None
    else:
        return numkey




odd = largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2])
odd2 =largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8])
odd3 =largest_odd_times([3, 0, 5, 3, 5, 3])
odd4 = largest_odd_times([3, 3, 2, 0])
odd5 = largest_odd_times([2, 2])
print(odd5)
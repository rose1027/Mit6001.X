def sum_digits(s):
    """ assumes s a string
            Returns an int that is the sum of all of the digits in s.
              If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sum = 0
    notInt = 0
    for c in s:
        try:
            i = int(c)
            #print(i)
            sum += int(c)
        except ValueError:
            notInt += 1

    if notInt != len(s):
         return sum
    else:
        raise ValueError

SUM = sum_digits("aob")
print(SUM)



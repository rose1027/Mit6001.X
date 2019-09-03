def sum_digits(s):
    sum = 0
    for c in s:
        try:
            i = int(c)
            #print(i)
            sum += int(c)
        except ValueError as err:
            pass
    return sum
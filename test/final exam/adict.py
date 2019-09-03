def uniqueValues(aDict):
    '''
        aDict: a dictionary
        If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
        If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
        returns: a sorted list of keys that map to unique aDict values, empty list if none
        '''
    #new dictionay the key is aDict.values
    unique = {}
    # list will save the sorted key later
    l = []
    #put aDict.values in Valueslist
    Values = []
    if aDict == {}:
        return []
    for v in aDict.values():
        if v not in unique.keys():
            unique[v] = 1
        else:
           unique[v] += 1
    for k,v in unique.items():
        #print(unique)
        if v == 1:
            Values.append(k)
    #print(newl)
    if Values == []:
        #print('**newlist is empty')
        return Values
    else:
       # print('newlist is not empty')
        for c in Values:
            #print('c=',c)
            for k,v in aDict.items():
                if c == v:
                   # print('v=',v,'k=',k)
                    l.append(k)


        return sorted(l)
#aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
bdict = {1: 1, 2: 1, 3: 1}
#l = uniqueValues(aDict)
l2 = uniqueValues(bdict)
#print(l)



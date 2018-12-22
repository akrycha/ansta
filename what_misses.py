def what_misses(list1, n):
    result = []
    for i in range(1,n+1):
        if not(i in list1):
            result.append(i)
    return result


what_misses([2, 4, 5], 10)

def sort_list(lst):

    j = len(lst)
    i = 1

    while (i < j):
        d = 0
        while (d <= j-1):
            if (lst[i] > lst[d]):
                lst[i], lst[d] = lst[d], lst[i]
            d += 1
        i += 1
    return lst
def sort_list(l):
    n = len(l)
    i = 1
    while(i < n):
        j = 0
        while(j <= n-i-1):
            if l[j+1] < l[j]:
               l[j+1], l[j] = l[j], l[j+1] 
            j = j+1
        i = i+1
    return l
            
l = [21, 54, 63, 11, 31, 44]
sort_list(l)
print(l)
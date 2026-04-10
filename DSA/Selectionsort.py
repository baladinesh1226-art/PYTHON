lst = [9,43,24,532,23,52,56,78,2,32,43,54]


for crt in range(len(lst)-1):
    min = crt
    for j in range(crt+1, len(lst)):
        if lst[min] > lst[j]:
            min = j


    lst[min], lst[crt] = lst[crt], lst[min]

print(lst)

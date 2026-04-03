def BinarySearch(lst, val):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = left + 1
        elif lst[mid] > val:
            right = mid - 1

    return -1

def LinearSearch(lst, val):
    for i, v in enumerate(lst):
        if v == val:
            print(i, v)
            break
    else:
        print(val, "is not present in the list")

def CountAccurrence(lst):
    dect ={}
    for val in lst:
        if val  in dect:
            dect[val] +=1
        else:
            dect[val]=1
    print("the first occurrence is:",list(dect.keys())[0],":", list(dect.values())[0])
    print(dect)


data_list = [
    "Apple", "Banana", "Cherry", "Apple", "Date",
    "Banana", "Elderberry", "Apple", "Cherry", "Date",
    "Apple", "Banana", "Apple", "Elderberry", "Date",
    "Cherry", "Apple", "Banana", "Elderberry", "Apple"
]

lst =[1,3,5,6,7,9,10,13,15,19,22,28,34,48,59,65,66,69]
val=5
print(BinarySearch(lst, val))
LinearSearch(lst, val)
print("=====count occurrences=====")
CountAccurrence(data_list)









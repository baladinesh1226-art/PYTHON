arr =[13,1,3,2,7,9,12]

for i in range(0,len(arr)-1):
    crt =i
    for j in range(1,len(arr)):
        if arr[j] < arr[crt]:
            arr[crt],arr[j] =arr[j], arr[crt]


print(arr)
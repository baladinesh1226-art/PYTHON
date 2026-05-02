arr =[1,2,3,4,5,6,7]

t =12
l =0
r=len(arr)-1
print(arr)
while l < r:
    val =arr[l] +arr[r]
    if val == t:
        print(arr[l], arr[r])
        break
    elif val > t:
        r =r-1
    elif val < t:
        l =l+1
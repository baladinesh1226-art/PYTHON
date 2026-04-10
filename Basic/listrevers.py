print("****Reversing an array in Python****")
arr = [1,2,3,4]

print("original array:", arr)

rev=arr[::-1]
print("reversed array using slice:", rev)

count =len(arr)-1
rev2 =[]

for i,n in enumerate(arr):
    rev2.append(arr[count])
    count-=1
print("reversed array using loop:", rev2)

rev3 =[]

for i in range(len(arr)-1, -1,-1):
    rev3.append(arr[i])
print("reversed array using range:", rev3)

rev4 = [arr[i] for i in range(len(arr)-1,-1,-1)]
print("reversed array using list comprehension:", rev4)


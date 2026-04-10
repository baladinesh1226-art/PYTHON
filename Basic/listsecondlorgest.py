arr = [10, 20, 5, 40, 30]
arr2=[]
max=0

print("****Finding the second largest element in an array****")
for val in arr:
	
	if val > max:
		arr2.append(val)
		max = val

print(arr2[-2])


print("****Finding the second largest element in an array without sorting****")


largest = secondlarg= float('-inf')

for num in arr:
	if num >largest:
		secondlarg=largest
		largest= num
	elif num > secondlarg and num != largest:
		num = secondlarg
		
print(secondlarg)


arr = [1, 2, 2, 3,3,1, 1]
freq = {}

for num in arr:
	if num in freq:
		freq[num]+=1
	else:
		freq[num]=1

print("frequency of each element:", freq)


print("max accuring element")

arr = [1, 2, 2, 3, 3, 3]
freq = {}

for num in arr:
	freq[num] = freq.get(num,0)+1
	print("freq:", freq.get(num,0))
	
max_key= max(freq, key=freq.get)
print("max_key:", max_key)




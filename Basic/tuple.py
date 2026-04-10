print("converting list to tuple")

lst =[1,2,3,4,5]
tup = tuple(lst)
print(tup)


print("count occurrences")

t = (1, 2, 2, 3, 2)
count = 0
for I in t:
	if I == 2:
		count+=1

print(count)

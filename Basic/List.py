fruits = ["apple", "banana"]
print("normal list", fruits)
fruits.append("mango")
print("append list", fruits)

print("==================================")

fruits = ["apple", "banana", "mango"]
print("normal list", fruits)
fruits.remove("banana")
print("remove list", fruits)

print("===================================")

fruits = ["apple", "banana", "mango"]
print("normal list", fruits)
fruits[1] = "orange"
print("Changed list", fruits) 

print("===================================")
print(" loop over num")
num = [10, 20, 30, 40]
for n in num:
    print(n)

print("===================================")

print("find largest number /n")
num =[29,45,75,12,67]
print("list for find max:",num)
largeest = num[0]

for n in num:
    if n > largeest:
        largeest=n

print("the largst number is:", largeest)

print("===================================")
print("find second largest num")
num =[29,45,75,12,67]
print("list for find second max:",num)

largest = num[0]
second_largest = num[0]
 
for n in num:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("the second largest number is:", second_largest)

print("===================================")
print("find sum of list")

num = [5,10, 15, 20]

print("list for find sum:", num)    
sum = 0 
for n in num:
    sum = sum + n

print("the sum is:", sum)


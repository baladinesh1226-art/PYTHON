print("method one")
a = 5
b = 10

a, b = b, a

print("a:", a)
print("b:", b)


print("method two")
a = 5
b = 10

a = a + b
b = a - b
a = a - b

print("a:", a)
print("b:", b)
student ={
    "name":"dinesh",
    "age":26,
    "city":"Orathanadu"
}

print("students:", student)

print("=================================")


print("loop through student:\n")
for key in student:
    print(key)

    
print("loop through value in student:\n")
for value in student.values():
    print(value)

print("loop through key and value in student:\n")
for key , value in student.items():
    print(key,":", value)


print("==========================" "\n")
student.pop("city")

print("after pop city:", student)
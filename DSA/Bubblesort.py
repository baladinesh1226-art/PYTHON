lst =[1,4,5,654,53,65,65,77,35]


# for i in range(0, len(lst)-1):
#     for j in range(0, len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] =lst[j+1],lst[j]
#

while True:
    a = True
    for j in range(0, len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] =lst[j+1],lst[j]
    if a:
        break

print(lst)
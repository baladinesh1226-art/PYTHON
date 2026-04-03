from collections import Counter

# s="vanakkammapla"
# freq ={}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] =1
#
# print(freq)
#
#
# nums=[1,2,3,4,5,6,8,9,10,12,16]
# n =len(nums)+1
#
# total = n * (n+1)//2
# miss_num = total - sum(nums)
#
# count=1
# missing_num =[]
#
# for n in nums:
#     while n != count:
#         missing_num.append(count)
#         count +=1
#     count+=1
#
# print(missing_num)
# print(miss_num)

# nums = [0,1,0,3,12]
#
# print("list for move zero to end", nums)
#
# j =0
#
# for i in range (len(nums)):
#     if nums[i] !=0:
#         nums[j],nums[i] = nums[i], nums[j]
#         j += 1
#
# print("move zero to end",nums)
#
#
# nums = [1,3,4,2,2,3]
# print("list for find duplicate", nums)
# dub = set()
# seen = set()
#
# for n in nums:
#     if n in seen:
#         dub.add(n)
#     else:
#         seen.add(n)
#
#
#
# print("duplicate:",dub )
#
# s1 = 'eat'
# s2 = 'tea'
# print("\n find anagram",s1,s2)
#
# if Counter(s1) == Counter(s2):
#     print("anagram")
# else:
#     print("not anagram")


s ="aabbcde"

freq = {}


for ch in s:
    freq[ch] = freq.get(ch, 0)+ 1

for ch in s:
    if freq[ch] ==1:
        print("first non-repeating:",ch)
        break


sng = "hello fried how are you"
print(sng,"the reversed string:",sng[::-1])



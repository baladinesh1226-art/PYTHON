# num =984937
# temp=0
# revnum=0

# while num>0:
# 	temp= num%10
# 	revnum=(revnum*10)+temp
# 	num=num//10

# print(revnum)




# num =10
# temp=0
# temp2=1
# print("fibonacci series ", temp, temp2, end=" ")
# for n in range(2,num):
# 	val=temp+temp2
# 	temp = temp2
# 	temp2 = val
	
# 	print(val,end=" ")
	
num1,num2 =36, 60
num1div=[]
val=[]

for n in range(1,(36//2)):
    if 36 % n==0:
        num1div.append(n)

for n in range(1,(60//2)):
    if 60 % n ==0 and n in num1div:
        val.append(n)

print(val[len(val)-1])





 
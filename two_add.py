a=input('l1:')[1:-1].split(",")
nums=[int(a[i]) for i in range(len(a))]
a1=input('l2:')[1:-1].split(",")
nums1=[int(a1[i]) for i in range(len(a1))]
sum=0
sum1=0
for i in range(len(nums)):
    x=10**i
    y=int(a[i])
    z=x*y
    sum=sum+z
#     sum=sum+int(a[i]*((10)**i))
for i in range(len(nums1)):
    x=10**i
    y=int(a1[i])
    z=x*y
    sum1=sum1+z
#     sum=sum+int(a[i]*((10)**i))
sum_add=sum+sum1
str=str(sum_add)
str1=str[::-1]
list=[]
for i in range(len(str)):
    list.append(int(str1[i]))
print(list)
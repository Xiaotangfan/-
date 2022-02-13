# nums=[2,7,11,15]
# target=9
# nums=[3,2,4]
# target=6
# nums=[3,3]
# target=6

a=input('列表:')[1:-1].split(",")
nums=[int(a[i]) for i in range(len(a))]
target=int(input("target"))
list=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==target:
            if i and j not in list:
                list.append(i)
                list.append(j)
list1=set(list)
list2=[]
for i in list1:
    list2.append(i)
print(list2)
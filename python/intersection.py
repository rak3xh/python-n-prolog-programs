list1=[1,2,3,4,5,6]
list2=[2,4,5,7,8]
list=[]
for i in range(len(list1)):
  for j in range(len(list2)):
     if list1[i]==list2[j]:
        list.append(list1[i])
print(list)
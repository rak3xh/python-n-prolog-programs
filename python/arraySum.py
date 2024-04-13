arr=[11,22,33,44,55]
sum=0
for i in range(len(arr)):
  if arr[i]%2==0:
    sum+=arr[i]
print(sum)
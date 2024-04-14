n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    s=input()
    arr.append(int(s))
max=arr[0]
for j in arr:
    if j>max:
        max=j 
print(max)        
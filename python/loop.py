"""for i in range(1,20,2):
    print(i)"""

"""
sum=0
for i in range(1,6):
    sum+=i
print(sum)"""

"""list=["rakesh","hero","KKR","dad","Thiruvanathapuram"]
max=0
for i in list:
    if(len(i)==3):
        print(i)

print(max)"""

k = ["name", "age", "id"]
v = ["rakesh", 23, 77]
dictionary = dict()
for i in k:
    for j in v:
        dictionary[i] = j
        v.remove(j)
        break
print(dictionary)

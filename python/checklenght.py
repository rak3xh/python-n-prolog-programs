n = int(input())
list = []

for i in range(n):
    s = input()
    list.append(s)
max = len(list[0])
for i in list:
    if len(i) > max:
        max = len(i)
print(max)

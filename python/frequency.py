nums = [10, 20, 32, 20, 21, 21, 13, 10]
dict = {}
for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

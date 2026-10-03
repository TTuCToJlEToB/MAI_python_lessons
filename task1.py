a = input()
res = {}
for i in set(a):
    res[f"{i}"] = a.count(i)
print(res)

from itertools import product
m = list(map(int, input().split()))
k, m = m[0], m[1]
a = []
for i in range(k):
    a.append(list(map(int, input().split()))[1:])
c = list(product(*a))
ans = []
for i in c:
    b = 0
    for j in i:
        b += j**2
    ans.append(b % m)

print(max(ans))

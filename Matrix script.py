import re
n,m = map(int, input().split())
l1 = []
for i in range(n):
    l1.append(input())
print(l1)
print(*l1)
l1 = list(zip(*l1))
print(l1)
s = ''
for i in l1:
    s += ''.join(i)
s =re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',s)
print(s)

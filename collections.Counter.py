from collections import Counter

user = int(input())
l1 = list(map(int, input().split()))

# print()
dict = Counter(l1)
userin = int(input())
p = 0
print(dict)
for i in range(userin):
    shoe, cost = list(map(int, input().split()))
    if dict[shoe]:
        dict[shoe] -= 1
        p = p + cost
        print(dict)


print(p)

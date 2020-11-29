from operator import itemgetter
n, m = input().split()
hello = []
for i in range(int(n)):
    hel = list(map(int, input().split()))
    hello.append(hel)

k = int(input())
array = sorted(hello, key=itemgetter(k))
for i in array:
    print(*i)

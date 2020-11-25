from collections import deque
user = int(input())
while user > 0:
    t = int(input())
    l1 = list(map(int, input().split()))
    t1 = deque(l1)
    lm = t1.popleft()
    rm = t1.pop()
    csv = lm if lm > rm else rm
    flag = False
    while len(t1) > 0:
        if lm >= rm and lm <= csv:
            csv = lm
            lm = t1.popleft()
            latest = lm
        elif rm >= lm and rm <= csv:
            csv = rm
            rm = t1.pop()
            latest = rm
        else:
            flag = True
            break

    if flag or latest > csv:
        print('No')
    else:
        print('Yes')

    user -= 1

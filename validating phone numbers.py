import re
pattern = r'^[789][0-9]+$'
user = int(input())
for i in range(user):
    user2 = input()

    if len(user2) > 10 or len(user2) < 10:
        print('NO')
    else:
        a = bool(re.search(pattern, user2))
        if a:

            print('YES')
        else:
            print('NO')

import re
userin = int(input())
for i in range(userin):
    m = user, mail = input().split()
    pattern = r'<[a-z][a-zA-z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}\>'
    if bool(re.match(pattern, mail)):
        print('this',user, mail)



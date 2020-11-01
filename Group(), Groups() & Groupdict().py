import re

a = input()
pattern = r'([a-zA-Z0-9])\1'
res  = re.search(pattern, a)
if res:
    print(res.group()[0])
else:
    print(-1)

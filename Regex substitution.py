import re
user = int(input())
for i in range(user):
    inp = input()
    s = re.sub(r"(?<= )&&(?= )", "and", inp)
    s = re.sub(r"(?<= )\|\|(?= )", "or", s)
    print(s)


import re
user = int(input())
css = False
for i in range(user):
    s = input()
    if '{' in s:
        css = True
    elif '}' in s:
        css = False
    elif css:
        print('sdsd',css)
        for colour in re.findall('#[a-zA-Z0-9]{3,6}', s):
            print(colour)
        


user_input = input().swapcase()
user_list = user_input.split()
string = ''
for i in range(len(user_list) - 1, -1, -1):
    string+= user_list[i]+' '

print(string)
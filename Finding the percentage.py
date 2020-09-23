data_dict = {}
n = int(input())

for i in range(n):
    user_marks = []
    user = input()
    for i in range(3):
        user_in = int(input())
        user_marks.append(user_in)
    data_dict.update({user: user_marks})

print(data_dict)
user_name = input()
result = data_dict.get(user_name)

average = (result[0] + result[1] + result[2])/3

print(average)

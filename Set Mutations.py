if __name__ == "__main__":
    user_inpu = int(input())
    user_list = list(map(int, input().split()))
    user_list = set(user_list)
    n = int(input())
    for i in range(n):
        user_input = input().split()
        if user_input[0] == 'intersection_update':
            new_list = list(map(int, input().split()))
            user_list.intersection_update(new_list)
        elif user_input[0] == 'symmetric_difference_update':
            new_list2 = list(map(int, input().split()))
            user_list.symmetric_difference_update(new_list2)
        elif user_input[0] == 'difference_update':
            new_list3 = list(map(int, input().split()))
            user_list.difference_update(new_list3)
        elif user_input[0] == 'update':
            new_list4 = list(map(int, input().split()))
            user_list.update(new_list4)
        else:
            print('Something gone wrong!')

    a = sum(user_list)
    print(a)
# Sample Input

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

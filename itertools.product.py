from itertools import product


def product_lists(A, B):

    a = list(product(A, B))
    convert_list = list(map(str, a))
    final_list = ' '.join(convert_list)
    return final_list


x = a1, *a2 = input().split()
y = b1, *b2 = input().split()
A = list(map(int, x))
B = list(map(int, y))

final_ans = product_lists(A, B)
print(final_ans)

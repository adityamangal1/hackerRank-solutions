'''
Author: Aditya Mangal 
Date:  24 september,2020
Purpose: python practise problem

'''

# find the secound runner up
user2 = list(map(int, input().split()))
print(user2)
list = [i for i in user2 if i != max(user2)]
print(max(list))




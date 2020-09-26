'''
Author: Aditya Mangal 
Date:  26 september,2020
Purpose: python practise problem

'''
def split_and_join(line):

    

    a = ('-'.join(line))
    return a


if __name__ == '__main__':
    line = input().split()
    result = split_and_join(line)
    print(result)





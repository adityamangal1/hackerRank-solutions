
'''
Author: Aditya Mangal 
Date:  25 september,2020
Purpose: python practise problem

'''
def swap_case(s):

    
    return (''.join([c.upper() if c.islower() else c.lower() for c in s]))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

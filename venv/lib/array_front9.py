'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.
'''
def array_front9(n):
    return 9 in n[:4]

result = array_front9([1,8,10,9,3])
print (result)
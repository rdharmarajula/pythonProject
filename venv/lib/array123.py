'''
Given an array of ints,
return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''
def array123(num):
    array1 = [1,2,3]
    for index in range(len(num)-2):
        array2 = num[index:index+3]
        print (array2)
        if array1 == array2:
            return True
    return False

result = array123([1,2,3])
print(result)
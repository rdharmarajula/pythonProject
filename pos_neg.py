def pos_neg(a, b, negative):
    if negative:
        return a < 0 > b
    else:
        return (a < 0 < b) or (a > 0 > b)

result = pos_neg(-10,1,True)
print (result)
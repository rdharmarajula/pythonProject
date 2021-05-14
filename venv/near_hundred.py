## absoulte always gives positive sign

def near_hundred(n):
    return (abs(100-n)<=10 or abs(200-n)<=10)

result = near_hundred(208)
print (result)

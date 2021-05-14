def front_back(str):
    if len(str) <= 1:
        return str
    middle_str = str[1:-1]
    return str[len(str)-1:] + middle_str + str[0]


result = front_back("rajesh")
print (result)
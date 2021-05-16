def string_spolsion(str):
    return_val = ''
    for index in range(len(str)+1):
        return_val += str[:index]
    return  return_val


result = string_spolsion('abc')
print (result)
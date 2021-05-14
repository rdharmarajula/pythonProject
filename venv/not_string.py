def not_string(str):
    if len(str) >= 3 and str[:3].upper() == 'NOT':
        return str
    return "not " + str


result = not_string("not rajesh")
print(result)

def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back


result = missing_char("rajesh", 10)
print(result)

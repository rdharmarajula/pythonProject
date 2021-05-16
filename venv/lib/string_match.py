def string_match(a, b):
    count = 0
    for index in range(len(a) - 1):
        if a[index:index + 2] == b[index:index + 2]:
            count += 1
    return count

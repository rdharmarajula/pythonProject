def is_8character_length(item):
    return len(item) <8

result = []
x = ['Python', 'programming', 'is', 'awesome!']
for i in x:
    if is_8character_length(i):
        result.append(i)
print (result)
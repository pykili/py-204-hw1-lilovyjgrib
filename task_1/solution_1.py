string = input()
b = int(string[0])
for a in string:
    c = int(a)
    if c > b:
        b = a
print(b)

string = input()
b = int(string[0])
for a in string:
  a = int(a)
  if a > b:
    b = a
print(b)

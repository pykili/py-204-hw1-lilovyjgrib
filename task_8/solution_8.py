n = int(input())
num = 1
summ = 0
i = 0
while num != 0:
    num = int(input())
    summ = summ + num
    i = i + 1
    if n == i + 1:
        num = 0
        print(0)
        print('это число должно быть нулём')
avg = summ/i
print(avg)

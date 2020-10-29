n = 1
while n < 101:
    summ = 0
    i = 1
    while i < n/2:
        summ = summ + 2*i - 1
        i = i + 1
    n = n + 1
    print(summ == n^2)

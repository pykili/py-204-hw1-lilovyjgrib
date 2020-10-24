# решение пока не работает на примерах с нечётным количеством одинаковых букв подряд
word = input()
occured_twice = False

d = ''
for t in word:
    bigram = d + t
    bigram_counter = 0
    n = ''
    if d != '':
        for m in word:
            bigram2 = n + m
            if n != '':
                if bigram2 == bigram:
                    bigram_counter += 1
                if bigram_counter == 2:
                    occured_twice = True

            n = m
    d = t
    print('\n')
print(occured_twice)

word = input()
rev_word = ''
len_count = 0
i_index = 0
a_index = 0

for letter in word:
    len_count += 1
for i in word:
    for a in word:
        if a_index == len_count - i_index - 1:
            rev_word += a
        a_index += 1
    a_index = 0
    i_index += 1
    
is_palindrom = rev_word == word
print(is_palindrom)
